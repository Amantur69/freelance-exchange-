from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Executor)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Ordering)
admin.site.register(Authoring)
admin.site.register(Message)
admin.site.register(Ticket)

# Register your models here.
