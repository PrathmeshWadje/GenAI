from django.contrib import admin
from .models import User
# Register your models here.
from unfold.admin import ModelAdmin

@admin.register(User)
class AdminUser(ModelAdmin):
    pass
