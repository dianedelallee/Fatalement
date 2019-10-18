from django.shortcuts import render, render_to_response
from django.template import RequestContext

from website.models.article import Article
from website.models.profile import Profile
from website.models.project import Project
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

    articles = article.get_paginate_articles(request, articles_find)

    return render(
            request, 'website/home.html',
            {'articles': articles}
    )


def project_detail(request, pk):
    project = Project.objects.get(id=pk)

    return render(
            request,
            'website/project_details.html',
            {'project': project}
    )


def project(request):
    all_projects = Project.objects.all()
    return render(
            request, 'website/projects.html',
            {'all_projects': all_projects}
    )


def eve(request):
    return render(
            request, 'website/eve.html'
    )


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
