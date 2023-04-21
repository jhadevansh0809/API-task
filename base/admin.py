from django.contrib import admin
from .models import CustomUser,ParagraphItem

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ParagraphItem)