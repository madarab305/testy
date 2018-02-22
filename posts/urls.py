from django.urls import path
from posts import views

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('update/', views.post_update, name='update'),
    path('delete/', views.post_delete, name='delete'),
    path('list/', views.post_list, name='list'),
    path('detail/', views.post_detail, name='detail'),
]