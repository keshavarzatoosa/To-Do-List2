from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
        ('Personal info', {'fields':('first_name', 'last_name')}),
        ('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


class CustomLoginView(LoginView):
    authentication_form = CustomUserLoginForm