from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import MemberProfile


class MemberProfileInline(admin.StackedInline):
    model = MemberProfile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = [MemberProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
