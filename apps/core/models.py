from django.db import models
from django.urls import reverse
from django.utils import timezone


class Car(models.Model):
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=8)
    vacant = models.BooleanField(default=True)

    def __str__(self):
        return self.model


class Order(models.Model):
    name = models.CharField(max_length=128)
    tel = models.CharField(max_length=17)
    address_from = models.CharField(max_length=128)
    address_to = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    desired_time = models.TimeField(default=timezone.now)
    car = models.ForeignKey(to=Car, on_delete=models.DO_NOTHING, related_name='car')

    def __str__(self):
        return self.name

    def end_order(self):
        vacant_car = Car.objects.filter(name=self.car)
        Order(car=vacant_car, vacant=True)

    def get_absolute_url(self):
        return reverse('core:order', kwargs={'pk': self.pk})
