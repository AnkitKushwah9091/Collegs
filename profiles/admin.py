from django.contrib import admin
from .models import UserProfileModel
# Register your models here.


@admin.register(UserProfileModel)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'gender' ,'religion','contact_no','home_town','current_city']


