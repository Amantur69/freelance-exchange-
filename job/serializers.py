from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ExecutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Executor
        fields = '__all__'


class CreateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    service_type_display = serializers.CharField(source='get_service_type_display')


    class Meta:
        model = Service
        fields = '__all__'


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    order_type_display = serializers.CharField(source='get_order_type_display')

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer

    class Meta:
        model = Order
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    service = ServiceSerializer()
    order = OrderSerializer()

    class Meta:
        model = Tag
        fields = '__all__'


class OrderingSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    customer = CustomerSerializer()
    service = ServiceSerializer()
    order = OrderSerializer()

    class Meta:
        model = Ordering
        fields = '__all__'


class CreateOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    customer = CustomerSerializer()
    severity = serializers.CharField(source='get_severity_display')

    class Meta:
        model = Ticket
        fields = '__all__'


class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    review = serializers.CharField(source='get_review_display')

    class Meta:
        model = Review
        fields = '__all__'
