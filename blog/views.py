from django.shortcuts import render

def render_articles(request):
    return render(request, 'articles.html')
