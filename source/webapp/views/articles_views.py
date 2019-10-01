from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from webapp.forms import ArticleForm
from webapp.models import Article, Comment


class IndexView(ListView):
    template_name = 'article/index.html'
    context_object_name = 'articles'
    model = Article
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class ArticleView(TemplateView):
    template_name = 'article/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_pk = kwargs.get('pk')
        context['comments'] = Comment.objects.filter(article=article_pk).order_by('-created_at')
        context['article'] = get_object_or_404(Article, pk=article_pk)
        # context['form'] = CommentForm()
        return context


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                category=form.cleaned_data['category']
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article/create.html', context={'form': form})


class ArticleUpdateView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        form = ArticleForm(data={
            'title': article.title,
            'author': article.author,
            'text': article.text,
            'category': article.category_id
        })
        return render(request, 'article/update.html', context={'form': form, 'article': article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.author = form.cleaned_data['author']
            article.text = form.cleaned_data['text']
            article.category = form.cleaned_data['category']
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article/update.html', context={'form': form, 'article': article})


class ArticleDeleteView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return render(request, 'article/delete.html', context={'article': article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        article.delete()
        return redirect('index')


