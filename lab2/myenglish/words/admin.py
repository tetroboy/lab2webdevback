from django.contrib import admin
from .models import Word
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'dob')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Word)
# Register your models here.
