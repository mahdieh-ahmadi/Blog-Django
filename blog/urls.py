from django.urls import path
from .views import HomePage, PostDetailPage

urlpatterns = [
    path('post/<int:pk>/' , PostDetailPage.as_view() , name='post_detail'),
    path('' , HomePage.as_view(), name='home'),
]