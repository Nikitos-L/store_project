from django.contrib import admin
from subscriptions.models import Tariffs, CustomUser, UserSubscriptions

# Register your models here.
admin.site.register(Tariffs)
admin.site.register(UserSubscriptions)

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'phone', 'tg_id']

admin.site.register(CustomUser, UserAdmin)
