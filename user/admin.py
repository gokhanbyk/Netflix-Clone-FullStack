from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (('Custom Fieldset', {'fields': ['phone', 'birth_date']}),)
    


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Profile)