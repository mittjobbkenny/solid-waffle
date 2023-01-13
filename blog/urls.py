from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/add/', views.PostAdd.as_view(), name='add_post'),
]
