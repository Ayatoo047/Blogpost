from django.contrib import admin

# Register your models here.
from .models import Blog, Message

admin.site.register(Blog)
# admin.site.register(Room)
admin.site.register(Message)