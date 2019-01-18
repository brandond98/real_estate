from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article

def index(request):
    news = Article.objects.order_by('-published_date').filter(is_published=True)
    paginator = Paginator(news, 6)
    page = request.GET.get('page')
    paged_news = paginator.get_page(page)
    context = {
        'news' : paged_news
    }
    return render (request, 'apps/news/news.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'apps/news/article.html', context)