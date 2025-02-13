from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"),
    path("posts", views.AllPostView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostVIew.as_view(), 
         name = "post-detail-page"), #posts/my-fist-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
] 