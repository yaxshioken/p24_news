from django.shortcuts import render, get_object_or_404
from django.views import View

from apps.account.models import Feed
from apps.article.models import Article, Category, Tag, Comment


class HomeView(View):
    def get(self, request):
        articles = Article.published.order_by('-published_at')
        first = articles.first()
        articles = articles[1:]
        tags = Tag.objects.all()

        if request.user.is_authenticated:
            comments = Comment.objects.filter(owner=request.user)
        else:
            comments = Comment.objects.none()
        context = {
            "article": first,
            "articles": articles,
            "tags": tags,
            "comment": comments,

        }
        return render(request, "article/index.html", context=context)




class CategoryView(View):
    def get(self, request, pk):
        category =Category.objects.get(id=pk)
        articles = Article.objects.filter(category=category)
        articles = Article.objects.filter(category__id=pk)
        context = {
            "articles": articles,
            # "tags": tags
        }
        return render(request, "article/index.html", context=context)


class ArticleDetialView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        comments = Comment.objects.filter(article=article).select_related('owner')
        context = {
            "article": article,
            "comments": comments,
        }
        return render(request, "article/article.html", context=context)
