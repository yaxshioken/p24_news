from django.urls import path

from apps.article.views import HomeView, CategoryView, ArticleDetialView

app_name = 'article'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<slug:slug>', ArticleDetialView.as_view(), name="article-detail"),
    path('category/<pk>/', CategoryView.as_view(), name="category")

]
