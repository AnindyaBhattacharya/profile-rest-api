from django.urls import path
from . import views

urlpatterns = [
    path('hello_apiview/', views.HelloView.as_view()),
]
