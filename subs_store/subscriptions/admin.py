from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from subscriptions.models import Tariffs, CustomUser, UserSubscriptions

# Register your models here.
admin.site.register(Tariffs)
admin.site.register(UserSubscriptions)
admin.site.register(CustomUser, UserAdmin)