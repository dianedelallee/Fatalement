from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from website.models.article import Article
from website.models.profile import Profile


def home(request):
    articles_list = Article.objects.all().order_by('-date', '-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(articles_list, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

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
