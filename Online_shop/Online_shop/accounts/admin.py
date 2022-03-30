from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Online_shop.accounts.models import ShopUser


class ProfileAdminConfig(UserAdmin):
    ordering = ('first_name',)
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff')


admin.site.register(ShopUser, ProfileAdminConfig)
