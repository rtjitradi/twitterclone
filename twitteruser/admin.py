from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitteruser.models import CustomUserModel
from twitteruser.forms import CustomUserChangeForm, CustomUserCreationForm


# Register your models here.
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
class CustomUserAdminModel(UserAdmin):
    model = CustomUserModel
    admin_addform = CustomUserCreationForm
    admin_changeform = CustomUserChangeForm
    displayfields_list = ['username', 'email']
    fieldsets = UserAdmin.fieldsets + (('More Details', {'fields': ('follow', )}),)


admin.site.register(CustomUserModel, CustomUserAdminModel)
