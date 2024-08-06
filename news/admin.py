from django.contrib import admin

# Register your models here.

from .models import News, Comments

class CommentsInLine(admin.TabularInline):
    model = Comments
    extra = 5

class AdminNews(admin.ModelAdmin):
    inlines = [CommentsInLine]
    list_display = ["title", "content", "created_at"]
    

admin.site.register(News, AdminNews)

