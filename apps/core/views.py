from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, FormView, ListView, DetailView, TemplateView, RedirectView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import OrderForm
from .models import Order, Car


class OrderFormView(FormView):
    template_name = 'core/index.html'
    form_class = OrderForm
    success_url = reverse_lazy('core:order_finish')

    def form_valid(self, form):
        order = form.save(commit=False)
        vacant_car = Car.objects.filter(vacant=True).first()
        print(vacant_car)
        if vacant_car is not None:
            vacant_car.vacant = False
            vacant_car.save()
            order.car = vacant_car
            order.save()
        else:
            return HttpResponse('<h1>Извините, все машины заняты. Повторите '
                                'попытку попозже.</h1>')
        return super().form_valid(form)


class OrderListView(ListView):
    template_name = 'core/order_list.html'
    queryset = Order.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_qs = Order.objects.all().order_by('-created_time')

        paginator = Paginator(object_list=order_qs, per_page=5)
        page = self.request.GET.get('page')

        try:
            order_list = paginator.page(page)
        except PageNotAnInteger:
            order_list = paginator.page(1)
        except EmptyPage:
            order_list = paginator.page(paginator.num_pages)

        context['order_list'] = order_list
        return context


class OrderDetailView(DetailView):
    template_name = 'core/order.html'
    model = Order
    context_object_name = 'order'


class OrderFinishDetailView(View):
    template_name = 'core/order_finish.html'
    model = Order
    context_object_name = 'order'


class EndOrderView(RedirectView):
    pattern_name = 'core:order_list'

    def get_redirect_url(self, *args, **kwargs):
        Order(self.request).end_order()
        return super().get_redirect_url(*args, **kwargs)
