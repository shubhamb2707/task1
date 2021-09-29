from django.db import models
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from base.models import *
from django.dispatch import receiver

# User model for creating users 
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(unique=True, max_length=14, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        """A meta object for defining name of the user table"""
        db_table = "User"

    # use User manager to manage create user and super user
    objects = UserManager()

    # define required fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']


#User COuntry Holiday Detail model 
class UserCountryHolidayInfo(models.Model):
    user_uuid = models.OneToOneField(
        User,
        on_delete=models.CASCADE,blank=True,null=True)
    geolocation_info = models.TextField(null=True, blank=True)
    holidays_info = models.TextField(null=True, blank=True)

#Post creation model..
class Post(BaseModel):
    of_user = models.ForeignKey(User,on_delete=models.CASCADE)
    postdata = models.TextField(null=True, blank=True)
    likecount = models.IntegerField(default=0,null=True)
    unlikecount = models.IntegerField(default=0,null=True)
    class Meta:
        """A meta object for defining name of the user table"""
        db_table = "PostTable"


#Like and Unlike Model
class LikeUnlike(BaseModel):
    user_of = models.ForeignKey(User,on_delete=models.CASCADE)
    post_user = models.ForeignKey(Post,on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    unlike  = models.BooleanField(default=False)

