from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, password) -> str:
        return make_password(password)



class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ["uuid","email","first_name","last_name"]



class GetPostSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='of_user.email')
    class Meta:
        model=Post
        fields = ['uuid','user_email','postdata','likecount','unlikecount']



class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = "__all__"



class LikeUnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=LikeUnlike
        fields = "__all__"