from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from apps.account.forms import SubscribeForm, FeedForm
from apps.account.models import Feed, Account
from apps.article.models import Comment


class SubscribeView(View):
    def get(self, request):
        form = SubscribeForm()

        context = {
            "form": form,
        }
        return render(request, "account/subscribe.html", context=context)

    def post(self, request):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article:home")
        else:
            context = {
                "form": form
            }
            return render(request, "account/subscribe.html", context=context)


class FeedView(View):
    def get(self, request):
        form = FeedForm()
        context = {
            "form": form
        }
        return render(request, "account/feed.html", context)

    def post(self, request):
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.account = request.user
            feed.save()
            return redirect("article:home")
        else:
            context = {
                "form": form
            }
            return render(request, "account/feed.html", context)
