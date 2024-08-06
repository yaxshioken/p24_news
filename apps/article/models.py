from django.db import models
from django.utils import timezone
from datetime import timedelta
from phonenumber_field.modelfields import PhoneNumberField
from apps.article.choices import Choices
from apps.shares.shared import BaseModel
from apps.account.models import Account

class Article(BaseModel):
    title = models.CharField(max_length=256, unique=True)
    body = models.CharField(max_length=1024, null=False)
    published_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Choices, default=Choices.DRAFT.value, max_length=15)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='apps/images')
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    like_count = models.IntegerField(default=0)

class Category(BaseModel):
    name = models.CharField(max_length=256)

class Comment(BaseModel):
    body = models.CharField(max_length=512)
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

def advertise_expire(*args, **kwargs):
    return timezone.now() + timedelta(days=3)

class Advertise(BaseModel):
    image = models.ImageField(upload_to='apps/advertise')
    link_url = models.URLField(blank=True, null=True)
    phone = PhoneNumberField(region='UZ')
    url = models.URLField()
    expire_date = models.DateTimeField(default=advertise_expire)
    is_active = models.BooleanField(default=False)
