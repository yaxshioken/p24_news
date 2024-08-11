from django.core.exceptions import ValidationError
from django.db.models import IntegerField, BigAutoField
from django.forms import Form, ModelForm, CharField, PasswordInput, Textarea, TextInput, EmailInput, EmailField, \
    URLField

from apps.account.models import Account, Feed


class SubscribeForm(ModelForm):
    password = CharField(widget=PasswordInput)
    confirm_password = CharField(widget=PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("confirm_password"):
            raise ValidationError("Passwords must be match")

    def save(self, commit=True):
        user: Account = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_subscribe = True
        user.save()
        return user

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "password", "confirm_password",)


class FeedForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    body = CharField(widget=Textarea())
    website = URLField(widget=TextInput())
    email = EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
    password = CharField(widget=PasswordInput)
    confirm_password = CharField(widget=PasswordInput)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords must match")
        return confirm_password

    def save(self, commit=True):
        feed: Feed = super().save(commit=False)
        feed.password = self.cleaned_data["password"]
        if commit:
            feed.save()

        return feed

    class Meta:
        model = Feed
        fields = ("id", "name", "body", "email", "password", "confirm_password")
