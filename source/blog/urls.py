from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, ArticleView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView, CommentCreateView, CommentView, CommentUpdateView, CommentDeleteView, CommentCreateViewFromArticle


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/add/', ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('comments/', CommentView.as_view(), name='comments'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/add/<int:pk>', CommentCreateViewFromArticle.as_view(), name='comment_add_from_article')
]
