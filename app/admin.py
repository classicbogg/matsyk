from django.contrib import admin

from .models import Category, Quote, Tag

# Регистрируем модели в админке Django
# После этого их видно на /admin/ и можно добавлять руками
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Quote)
