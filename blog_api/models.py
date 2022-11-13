from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(blank=False, null=False, unique=True)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"
        
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
class Article(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(blank=False, null=False, unique=True)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    
    class Meta: 
        ordering = ('-created_at',)
        verbose_name_plural = 'Articles'
        
    def __str__(self) -> str:
        return self.title
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
    
    
