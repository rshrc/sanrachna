from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser, Profile
from sanrachna.settings import ADMIN_SITE_HEADER, ADMIN_SITE_TITLE

admin.site.site_header = ADMIN_SITE_HEADER
admin.site.site_title = ADMIN_SITE_TITLE


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'username', 'email', 'name']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'birth_date', 'city', 'country']
