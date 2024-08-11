from django.urls import path

from apps.account.views import SubscribeView
from apps.account.views import FeedView

app_name = "account"
urlpatterns = [
    path('subcribe/', SubscribeView.as_view(), name="subscribe"),
    path('feed/', FeedView.as_view(), name='feed')
]
