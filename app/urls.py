from django.urls import path

from . import views

# Здесь адреса связываются с функциями из views.py
# Например: /quotes/, /quote/1/, /categories/create/
urlpatterns = [
    path("quotes/", views.get_quotes, name="get_quotes"),
    path("quote/<int:pk>/", views.get_quote, name="get_quote"),
    path("quotes/create/", views.create_quote, name="create_quote"),

    path("categories/", views.get_categories, name="get_categories"),
    path("category/<int:pk>/", views.get_category, name="get_category"),
    path("categories/create/", views.create_category, name="create_category"),

    path("tags/", views.get_tags, name="get_tags"),
    path("tag/<int:pk>/", views.get_tag, name="get_tag"),
    path("tags/create/", views.create_tag, name="create_tag"),
]
