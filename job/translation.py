from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('rating', 'description')



@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
