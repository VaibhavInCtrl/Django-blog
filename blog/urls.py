from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="blogs-home"),
    path("detail/", views.detail, name= "blogs-detail")
]