from django.contrib import admin

# Register your models here.
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_text', 'date')
    list_filter = ['date']
    search_fields = ['message_text']

admin.site.register(Message, MessageAdmin)
