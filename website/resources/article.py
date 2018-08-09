from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from website.models.article import Article

def get_paginate_articles(request, articles_list):
    page = request.GET.get('page', 1)
    paginator = Paginator(articles_list, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return articles


def get_articles_according_to_search(list_of_words):
    all_articles = Article.objects.all()
    articles_find = []
    for art in all_articles:
        split_title = art.name.split(' ')
        split_tags = art.tags.split(',')
        for word in list_of_words:
            if word in split_tags or word in split_title:
                articles_find.append(art)
    return articles_find
