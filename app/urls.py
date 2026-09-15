from django.urls import path
from . import views

urlpatterns = [
    path('quote/<int:pk>/', views.get_quote, name='get_quote'),
]
