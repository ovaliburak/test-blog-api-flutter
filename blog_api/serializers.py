from rest_framework.serializers import ModelSerializer, CharField, PrimaryKeyRelatedField
from . import models

class CategoryApiSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"

class CategoryCreateApiSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["title"]
        

class ArticleApiSerializer(ModelSerializer):
    category = CharField(source="category.title", read_only=True)
    class Meta:
        model = models.Article
        fields = "__all__"

class ArticleCreateApiSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = ["title", "content", "category"]

class CategoryArticleListSerializer(ModelSerializer):
    article = ArticleApiSerializer(many=True, read_only=True)
    class Meta: 
        model = models.Category
        fields = ["title", "article"]