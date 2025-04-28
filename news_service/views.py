from django.http import JsonResponse
from .newsUtil import get_news
from django.views.decorators.http import require_http_methods
from .models import Article
from django.core import serializers
from .serializers import ArticleSerializer
from rest_framework.views import APIView
class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
def gen_articles(request):
    print("Fetching satirical articles...")
    try:
        print("Fetching satirical articles still")
        # Fetch the latest satirical articles
        articles = get_news()
        print(articles)
        # Save the articles to the database
        for article in articles:
            print("Saving satirical article...", article['title'])
            new_article = Article.objects.create(
                title=article['title'],
                body=article['body_text'],
                tags=article['tags']
            )
            
            new_article.save()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    serialized_articles = serializers.serialize('json', Article.objects.all())
    return JsonResponse(serialized_articles, safe=False)