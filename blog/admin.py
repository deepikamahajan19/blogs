from django.contrib import admin
from .models import Post,Comment,Categ,Notifications,Events

class Filter(admin.ModelAdmin):
    list_filter=('author','status','review')

admin.site.register(Post,Filter)
admin.site.register(Comment)
admin.site.register(Categ)
admin.site.register(Notifications)
admin.site.register(Events)
