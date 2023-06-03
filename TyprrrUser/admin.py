from django.contrib import admin
from .models import TyprrrUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    ordering = ('-created',)
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    list_display = ('email', 'is_active', 'is_staff',)
    fieldsets = (
        ('Userinfo', {'fields': ('username', 'email', 'is_active')}),
        ('Stats', {'fields': ('races_completed', 'average_speed', 'races_won', 
                              'best_speed', )})
    )

admin.site.register(TyprrrUser, UserAdminConfig)
