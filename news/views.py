from django.shortcuts import render
from news.models import News


def news(request):

    featured_news = News.objects.filter(is_featured=True).order_by('-created_at')
    other_news = News.objects.filter(is_featured=False).order_by('-created_at')

    context = {
        "last_featured_news": featured_news[0],
        "featured_news": featured_news[1:6],
        "other_news": other_news,
    }

    return render(request, 'news/news.html', context=context)
