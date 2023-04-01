from django.urls import path
from .views import HomePage, PostDetailPage, NewPostPage, EditPostPage, DeletePostPage

urlpatterns = [
    path('post/<int:pk>/delete/', DeletePostPage.as_view(), name='post_delete'),
    path('post/edit/<int:pk>/',EditPostPage.as_view(), name='post_edit' ),
    path('post/new', NewPostPage.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailPage.as_view(), name='post_detail'),
    path('', HomePage.as_view(), name='home'),
]
