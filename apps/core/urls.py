from django.urls import path

from .views import OrderFormView, OrderListView, \
    OrderDetailView, OrderFinishDetailView, EndOrderView


app_name = 'core'

urlpatterns = [
    path('', OrderFormView.as_view(), name='index'),
    path('endorder/', EndOrderView.as_view(), name='end_order'),
    path('orderfinish/', OrderFinishDetailView.as_view(), name='order_finish'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<pk>/', OrderDetailView.as_view(), name='order'),
]
