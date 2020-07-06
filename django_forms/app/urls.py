from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.formPost),
    path('snippet', views.snippet_detail),
]