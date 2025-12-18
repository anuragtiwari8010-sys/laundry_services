from django.shortcuts import render
from BlogArticles.models import Article

def get_blog_articles(request):
    """Get all blog articles and pass to template"""
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})

def get_article_detail(request, article_id):
    """Get single article detail"""
    try:
        article = Article.objects.get(id=article_id)
        article.views += 1
        article.save()
        return render(request, 'single.html', {'article': article})
    except Article.DoesNotExist:
        return render(request, 'single.html', {'error': 'Article not found'}, status=404)
