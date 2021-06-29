from django.contrib import admin
from .models import Profile
class Filter(admin.ModelAdmin):
    list_filter=('status','review')

admin.site.register(Profile,Filter)
