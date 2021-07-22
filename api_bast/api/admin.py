
from django.contrib import admin

from .models import Account


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username',
                    'address', 'last_name', 'first_name', 'profile_image')

    empty_value_display = '-empty-'


admin.site.register(Account, UserAdmin)
