from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "{} , phone: {}".format(self.user, self.phone)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "{} , phone: {}".format(self.user, self.phone)



class Service(models.Model):
    SERVICE_TYPES = [
        ('1', _('Веб разработка')),
        ('2', _('Дизайн')),
        ('3', _('Маркетинг')),
        ('4', _('Копирайтинг')),
        ('5', _('Рерайтинг')),
        ('6', _('Видеомонтаж')),
        ('7', _('Фотошоп')),
    ]
    title = serializers.CharField(label=_("Job Title"))
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(_('Название'), max_length=99)
    description = models.TextField(_('Описание'))
    service_type = models.CharField(_('Тип услуги'), choices=SERVICE_TYPES, default='1', max_length=1)
    price = models.IntegerField(_('Цена'))
    title = _("This is a translatable string")

    def __str__(self):
        return '{}, {}, цена: {}'.format(self.name, self.get_service_type_display(), self.price)


class Order(models.Model):
    ORDER_TYPE = [
        ('1', 'Веб разработка'),
        ('2', 'Дизайн'),
        ('3', 'Маркетинг'),
        ('4', 'Копирайтинг'),
        ('5', 'Рерайтинг'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотошоп'),

    ]
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=99)
    description = models.TextField()
    order_type = models.CharField(choices=ORDER_TYPE, default=1, max_length=1)
    price = models.IntegerField()

    def __str__(self):
        return '{}, {}, price: {}'.format(self.name, self.get_order_type_display(), self.price)


class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete= models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)


class Ordering(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        '{} - {} ,Customer: {}, Executor: {}'.format(self.order_date, self.deadline ,self.customer, self.executor)


class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    message_date = models.DateTimeField()
    is_edited = models.BooleanField(default=False)
    description = models.TextField()


class Ticket(models.Model):
    SEVERITIES = [
        ('1', "Низкая"),
        ('2', 'Cредняя'),
        ('3', 'Высокая')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default=1, max_length=1)
    description = models.TextField()
    is_resolved = models.BooleanField(default=False)


class Review(models.Model):
    RATING_FILLED = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ]
    rating = models.CharField(choices=RATING_FILLED, default=1, max_length=1)
    description = models.TextField()


class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null= True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null= True)






