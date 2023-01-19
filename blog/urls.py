from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/add/', views.PostAdd.as_view(), name='add_post'),
    path('<slug:slug>/<int:pk>/update/', views.PostUpdate.as_view(), name='update_post'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='delete_post'),
    path("search/", views.SearchResults.as_view(), name='search_results')
]
