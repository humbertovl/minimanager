from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.currency import Currency
from .models.user import User

admin.site.register(User, UserAdmin)
admin.site.register(Currency)
