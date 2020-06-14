from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name = "post_new"),
    path('post/<int:pk>/edit/<int:draft>', views.post_edit, name = "post_edit"),
    path('drafts/', views.post_draft_list, name = "post_draft_list"),
    path('post/<pk>/publish', views.post_publish, name = "post_publish"),
    path('post/<pk>/unpublish', views.post_unpublish, name = "post_unpublish"),
    path('post/<pk>/delete', views.post_delete, name = "post_delete"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>/delete', views.delete_comment, name='delete_comment'),
]
