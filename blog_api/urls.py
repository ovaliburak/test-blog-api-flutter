from django.urls import path
from . import views
urlpatterns = [
    path('articles/', views.get_articles, name="get_articles"),
    path('article/create/', views.PostArticle.as_view(), name='post_article'),
    path('article/delete/<slug:slug>/', views.DestroyArticle.as_view(), name="destroy_article"),
    path('article/<slug:slug>/', views.get_article, name="get_article"),
    path('categories/', views.get_categories, name="get_categories"),
    path('categories/articles/', views.CategoryArticleList.as_view(), name="get_articles_by_category"),
    path('category/create/', views.PostCategory.as_view(), name='post_category'),
    path('category/delete/<slug:slug>/', views.DestroyCategory.as_view(), name="destroy_category"),
    path('category/<slug:slug>/', views.get_category, name="get_category"),
    
    
]
