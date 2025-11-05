from django.contrib import admin
from .models import ContactMessage
@admin.register(ContactMessage)
# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    