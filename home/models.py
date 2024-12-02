from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager
from datetime import datetime
# Create your models here.

class CustomUser(AbstractUser):
    username=models.CharField(max_length=15,default='SuperUser',unique=True)
    name=models.CharField(max_length=20,default=0)
    year=models.IntegerField(default=5)
    email=models.EmailField("email_address",unique=True)
    domain1=models.CharField(max_length=20,blank=True,null=True)
    domain2=models.CharField(max_length=20,blank=True,null=True)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username', 'name', 'year']
    objects=CustomManager()

    def __str__(self):
        return self.username
    


#for hashing pass directly of admin
# from home.models import CustomUser

# users = CustomUser.objects.all()
# for user in users:
#     if len(user.password) < 50:
#         print(f"Hashing password for user: {user.email}")
#         user.set_password(user.password)
#         user.save()