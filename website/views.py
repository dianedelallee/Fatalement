from django.shortcuts import render

from website.models.article import Article

def home(request):

    articles = Article.objects.all().order_by('-date', '-id')


    return render(
        request, 'website/home.html',
        {'articles': articles}
    )
