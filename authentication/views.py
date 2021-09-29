import datetime
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings 
from rest_framework.permissions import IsAuthenticated   
from datetime import date
import holidays
import requests
import json
from requests import get
from .tasks import helper

# Response Data Function here for gtting response
def responsedata(status, message, data=None):
    if status:
        return {"status": status, "message": message, "data": data}
    else:
        return {"status": status, "message": message}

# view for sign Up User
class SignUp(TokenObtainPairView):
    def post(self, request):
        # import pdb; pdb.set_trace()
        if not request.data.get('email'):
            return Response(responsedata(False, "Email id is required"), status=status.HTTP_200_OK)

        if User.objects.filter(email=request.data.get('email')).exists():
            return Response(responsedata(False, "Email id already exists"), status=status.HTTP_200_OK)

        if not request.data.get('password'):
            return Response(responsedata(False, "Password is required"), status=status.HTTP_200_OK)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            uuid = serializer.data["uuid"]
            tokenserializer = TokenObtainPairSerializer(data={"email": request.data.get(
                "email"), "password": request.data.get("password")})
            if tokenserializer.is_valid(raise_exception=True):
                data = tokenserializer.validate({"email": request.data.get(
                    "email"), "password": request.data.get("password")})
                data.update(serializer.data)
                helper.delay(uuid)
                return Response(responsedata(True, "Signup successfull", data), status=status.HTTP_200_OK)
        else:
            return Response(responsedata(False, "serializer error"), status=status.HTTP_400_BAD_REQUEST)
        return Response(responsedata(False, "Something went wrong"), status=status.HTTP_400_BAD_REQUEST)

#view for login user
class Login(APIView):
    def post(self,request):
        user = User.objects.none()
        if User.objects.filter(email=request.data.get('email')).exists():
            user = User.objects.get(email=request.data.get('email'))
        if User.objects.filter(mobile=request.data.get('email')).exists():
            user = User.objects.get(mobile=request.data.get('email'))
        if user:
            if user.check_password(request.data.get('password')):
                token = RefreshToken.for_user(user)
                user.last_login = datetime.datetime.now()
                user.save()
                data = dict(accessToken=str(token.access_token),
                            email=user.email,
                            last_login=user.last_login,
                            uuid=user.uuid,)

                return Response(data)
            else:
                    return Response(responsedata(False, "Password is incorrect"), status=status.HTTP_200_OK)
        else:
            return Response(responsedata(False, "User does not exist"), status=status.HTTP_200_OK)

#Post creation view
class CreatePost(APIView):
    #method for creating post
    def post(self, request):
        if request.user.is_authenticated:
            data = request.data
            ser = CreatePostSerializer(data=data)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(responsedata(True, "post created", ser.data), status=status.HTTP_201_CREATED)
            else:
                return Response(responsedata(False, "Could not create post"), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(responsedata(False, "invalid user"), status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        #mehtod for retrieving all Users Post 
        if request.user.is_authenticated:
            post = Post.objects.all()    
            ser = GetPostSerializer(post,many=True).data
            return Response(responsedata(True, "All Post Retrieved", ser), status=status.HTTP_200_OK)
        else:
            return Response(responsedata(False, "invalid user"), status=status.HTTP_400_BAD_REQUEST)

   
#view for getting all users 
class GetUsers(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            usr = User.objects.all()
            ser = ShowUserSerializer(usr,many=True).data
            return Response(responsedata(True, "All User Retrieved", ser), status=status.HTTP_200_OK)
        else:
            return Response(responsedata(False, "invalid user"), status=status.HTTP_400_BAD_REQUEST)

#view for like and unlike post 
class CreateLikeUnlike(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            data = request.data
            ser = LikeUnlikeSerializer(data=data)
            if ser.is_valid(raise_exception=True):
                ser.save()
                ins = Post.objects.get(uuid=data["post_user"])
                if data["like"] == True:
                    ins.likecount = ins.likecount+1
                    ins.save()
                if data["unlike"] == True:
                    ins.unlikecount = ins.unlikecount+1
                    ins.save()
                return Response(responsedata(True, "post created", ser.data), status=status.HTTP_201_CREATED)
            else:
                return Response(responsedata(False, "Could not create post"), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(responsedata(False, "invalid user"), status=status.HTTP_400_BAD_REQUEST)

