from django.contrib import admin
from django.contrib.auth.admin import User
from userprofile.models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'pix', 'email', 'phone', 'address', 'dob', 'nationality', 'gender', 'state']
admin.site.register(Profile, ProfileAdmin)
