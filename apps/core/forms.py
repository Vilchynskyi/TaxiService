from django import forms
from .models import Order
from .validators import cyrillic, tel_number


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           validators=[cyrillic],
                           label='Имя')
    tel = forms.CharField(max_length=17,
                          validators=[tel_number],
                          label='Телефон')
    address_from = forms.CharField(max_length=128, label='Адрес отправление')
    address_to = forms.CharField(max_length=128, label='Адрес прибытия')
    desired_time = forms.TimeField(label='Желаемое время подачи авто',
                                   help_text='Указывайте время в формате 00:00')
    id = forms.HiddenInput()

    class Meta:
       model = Order
       fields = ['name', 'tel', 'address_from', 'address_to', 'desired_time']
