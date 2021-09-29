from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('post/', CreatePost.as_view(), name='post'),
    path('allusers/', GetUsers.as_view(), name='alluser'),
    path('likeunlike/', CreateLikeUnlike.as_view(), name='likeunlike'),
]