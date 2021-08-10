from django.urls import path

from likeapp.views import LikeView

app_name='likeapp'

urlpatterns=[



    path('article/like/<int:pk>',LikeView.as_view(),name='article_like'),



]