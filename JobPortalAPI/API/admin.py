from django.contrib import admin
from .models import *
from .models import Profile

# Register your models here.
admin.site.register(Company)
admin.site.register(Candidates)
admin.site.register(Profile)
