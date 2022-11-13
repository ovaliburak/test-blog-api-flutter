from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView

@api_view(['GET'])
def get_articles(request):
    articles = models.Article.objects.all()
    serializer = serializers.ArticleApiSerializer(articles, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def get_article(request, slug):
    article = models.Article.objects.get(slug=slug)
    serializer = serializers.ArticleApiSerializer(article, many=False)
    return Response(serializer.data)

class PostArticle(CreateAPIView):
    serializer_class = serializers.ArticleCreateApiSerializer
    model = models.Article

class DestroyArticle(DestroyAPIView):
    serializer_class = serializers.ArticleApiSerializer
    model = models.Article
    lookup_field = "slug"
    queryset = models.Article.objects.all()

class CategoryArticleList(ListAPIView):
    serializer_class = serializers.CategoryArticleListSerializer
    queryset = models.Category.objects.all()
   
    
@api_view(['GET'])
def get_categories(request):
    categories = models.Category.objects.all()
    serializer = serializers.CategoryApiSerializer(categories, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def get_category(request, slug):
    category = models.Category.objects.get(slug=slug)
    serializer = serializers.CategoryApiSerializer(category, many=False)
    return Response(serializer.data)

class PostCategory(CreateAPIView):
    serializer_class = serializers.CategoryCreateApiSerializer
    model = models.Category

class DestroyCategory(DestroyAPIView):
    serializer_class = serializers.CategoryApiSerializer
    model = models.Category
    lookup_field = "slug"
    queryset = models.Category.objects.all()
    
