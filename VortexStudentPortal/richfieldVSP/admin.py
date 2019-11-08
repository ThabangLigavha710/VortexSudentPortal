from django.contrib import admin
from .models import Search
from .models import create_user

# Register your models here.
admin.site.register(Search)
admin.site.register(create_user)