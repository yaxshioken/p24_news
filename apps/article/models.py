from datetime import timedelta

from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import CharField, SlugField, TextField, DateTimeField, TextChoices, Manager, ForeignKey, CASCADE, \
    IntegerField, ImageField, SET_NULL, URLField, BooleanField, ManyToManyField
from django.utils import timezone
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

from apps.article.choices import Status
from apps.article.managers import PublishManager, ActiveAdvertiseManager
from apps.shared.models import BaseModel


class Article(BaseModel):
    # managers
    objects = Manager()
    published = PublishManager()

    # fields
    title = CharField(max_length=256)
    slug = SlugField(unique=True, blank=True, max_length=256)
    body = RichTextUploadingField()
    published_at = DateTimeField(default=timezone.now)
    status = CharField(max_length=15, choices=Status, default=Status.DRAFT)
    category = ForeignKey("article.Category", CASCADE, 'artcicles')
    likes = IntegerField(default=0)
    owner = ForeignKey("account.Account", SET_NULL, 'article', null=True)
    is_active = BooleanField(default=False)
    tags = ManyToManyField("article.Tag", "articles")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(" ".join([self.published_at.strftime('%Y-%m-%d'), self.title]))
        super().save(force_insert, force_update, using, update_fields)


class Category(BaseModel):
    name = CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Comment(BaseModel):
    body = TextField()
    owner = ForeignKey("account.Account", CASCADE, "comments")
    article = ForeignKey("article.Article", CASCADE, "comments")


def advertise_expire(*args, **kwargs):
    return timezone.now() + timedelta(days=3)


class Advertise(BaseModel):
    active = ActiveAdvertiseManager()
    image = ImageField(upload_to="advertise/images/")
    url = URLField()
    expire_date = DateTimeField(default=advertise_expire)
    phone = PhoneNumberField(region="UZ")
    is_active = BooleanField()



class Tag(BaseModel):
    name = CharField(max_length=56)

    def __str__(self):
        return self.name
