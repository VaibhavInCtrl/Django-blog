from os import name
from django.urls import path
from .views import PostClassView, PostDetailView, PostCreateForm, PostUpdateForm, PostDeleteView, UserPostClassView
from . import views
urlpatterns = [
    #path("", views.home, name="blogs-home"),
    path('', PostClassView.as_view(),name = 'blogs-home'),
    path("detail/", views.detail, name= "blogs-detail"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('create/', PostCreateForm.as_view(), name='create-post'),
    path('post/<int:pk>/update/',PostUpdateForm.as_view(), name = 'update-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'delete-post'),
    path('user/<str:username>/', UserPostClassView.as_view(), name = 'user-posts')
]