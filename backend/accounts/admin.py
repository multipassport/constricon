from accounts.models import UserAccount
from django.contrib import admin


@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'email',
        'avatar',
        'public_name',
    ]
