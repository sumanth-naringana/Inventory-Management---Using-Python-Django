from django.contrib import admin

from user.views import profile
from .models import Profile

# Register your models here.
admin.site.register(Profile)
