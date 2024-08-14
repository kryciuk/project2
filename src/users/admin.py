# from django.contrib import admin
#
# from users.models import Profile
#
# admin.site.register(Profile)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomInvitation, CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (("Custom Fields", {"fields": ("building",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Custom Fields", {"fields": ("building",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomInvitation)
