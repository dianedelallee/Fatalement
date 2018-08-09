from django.shortcuts import render

from website.models.article import Article
from website.models.profile import Profile
from website.resources import article


def home(request):
    articles_list = Article.objects.all().order_by('-date', '-id')
    articles = article.get_paginate_articles(request, articles_list)

    return render(
        request, 'website/home.html',
        {'articles': articles}
    )


def about(request):
    my_profile = Profile.objects.get(name='dianedelallee')
    return render(
        request, 'website/about.html',
        {'my_profile': my_profile}
    )


def details_page(request, pk):
    article = Article.objects.get(id=pk)
    return render(
        request, 'website/details_article.html',
        {'article': article}
    )

def search(request):
    words_to_find = request.GET.get('search').split(' ')
    articles_find = article.get_articles_according_to_search(words_to_find)

    articles =  article.get_paginate_articles(request, articles_find)


    return render(
        request, 'website/home.html',
        {'articles': articles}
    )