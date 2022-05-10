from django.contrib import admin

# Register your models here.
from .models import News, Url
class UrlAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['link']
# class NewsAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("News", {"fields": ["title", "link", "published"]}),
#         ("DB Dates", {"fields": ["created_at, updated_at"]}),
#         ("Source", {"fields": ["source"]}),
#     ]


admin.site.register(News)
admin.site.register(Url, UrlAdmin)
