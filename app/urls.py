from django.urls import path

from . import views

urlpatterns = [
    # Цитаты
    path("quotes/", views.QuoteList.as_view(), name="quote_list"),
    path("quotes/<int:pk>/", views.QuoteDetail.as_view(), name="quote_detail"),

    # Категории
    path("categories/", views.CategoryList.as_view(), name="category_list"),
    path("categories/<int:pk>/", views.CategoryDetail.as_view(), name="category_detail"),

    # Теги
    path("tags/", views.TagList.as_view(), name="tag_list"),
    path("tags/<int:pk>/", views.TagDetail.as_view(), name="tag_detail"),
]
