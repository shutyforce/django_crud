from django.urls import path
from .import views 

urlpatterns = [
    path('', views.PostList.as_view(), name='blog_home'),
    path('post/new/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]
