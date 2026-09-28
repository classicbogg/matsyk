from django.contrib import admin

from .models import Category, Quote, Tag
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Quote)
