from rest_framework import viewsets
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import *
from django.utils.translation import  activate
from django.utils.translation import gettext_lazy as _


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateExecutorSerializer
        return ExecutorSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCustomerSerializer
        return CustomerSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ServiceFilter # Добавляем DjangoFilterBackend для фильтрации
    filterset_fields = ['price']  # Указываем поля, по которым можно фильтровать
    ordering_fields = ['price']  # Указываем поля, по которым можно сортировать
    ordering = ['price']  # По умолчанию сортировка по цене
    title = models.CharField(max_length=255, verbose_name=_("Job Title"))

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateServiceSerializer  # Используем другой сериализатор для создания
        return ServiceSerializer


    def get_queryset(self):
        # Получаем язык из GET-параметра, если его нет — по умолчанию 'en'
        language = self.request.GET.get('lang', 'en')
        activate(language)  # Активируем нужный язык

        # Возвращаем базовый queryset
        queryset = Service.objects.all()

        # Здесь можно добавить логику фильтрации или других операций, если нужно.
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderSerializer
        return OrderSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMessageSerializer
        return MessageSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTicketSerializer
        return TicketSerializer


class OrderingViewSet(viewsets.ModelViewSet):
    queryset = Ordering.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderingSerializer
        return OrderingSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer