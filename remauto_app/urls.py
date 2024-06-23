from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.main, name="main"),
    path('form/', views.create_client, name='create_client'),
    path('login/', views.login,name='login'),
]