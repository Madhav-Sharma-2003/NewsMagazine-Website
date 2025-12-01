from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'comment', 'created_at']  # yahan sirf field names

admin.site.register(Comment, CommentAdmin)
