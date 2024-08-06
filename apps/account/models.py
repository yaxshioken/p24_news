from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField,ForeignKey,URLField,CASCADE
from apps.account.choices import RoleChoices
from apps.account.shared import BaseModel

class Account(AbstractUser,BaseModel):
    role=CharField(max_length=256,default=RoleChoices.MEMBER.value)

class Blog(BaseModel):
    title=CharField(max_length=256,null=False,unique=True)
    body=CharField(max_length=1024,null=False)
    image=ImageField(upload_to='apps.account/images')
    customer=ForeignKey(Account,on_delete=CASCADE)



class Feed(BaseModel):
    name=CharField(max_length=64,null=False)
    body=CharField(max_length=512)
    website=URLField(blank=True,null=False)
    owner=ForeignKey(Account,on_delete=CASCADE)