from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import CommentForm
from webapp.models import Article, Comment


class CommentCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, 'comment/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                article=form.cleaned_data['article']
            )
            return redirect('article_view', pk=comment.article.pk)
        else:
            return render(request, 'comment/create.html', context={'form': form})


class CommentView(TemplateView):
    template_name = 'comment/comments_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('-created_at')
        return context


class CommentUpdateView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        form = CommentForm(data={
            'article': comment.article.id,
            'author': comment.author,
            'text': comment.text
        })
        return render(request, 'comment/update.html', context={'form': form, 'comment': comment})

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment.article = form.cleaned_data['article']
            comment.author = form.cleaned_data['author']
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('comments')
        else:
            return render(request, 'comment/update.html', context={'form': form, 'comment': comment})


class CommentDeleteView(View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        comment.delete()
        return redirect('comments')


class CommentCreateViewFromArticle(View):
    def post(self, request, *args, **kwargs):
        article_id = get_object_or_404(Article, pk=kwargs.get('pk'))
        author = request.POST.get('author')
        text = request.POST.get('text')
        comment = Comment.objects.create(
            author=author,
            text=text,
            article=article_id
        )

        return redirect('article_view', pk=comment.article.pk)
