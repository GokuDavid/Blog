from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdown import Markdown

class Article(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='articles')

    def get_md(self):
        md=Markdown(
            extensions=[
                'markdown.extensions.extra', 
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body=md.convert(self.body)
        return md_body,md.toc

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created']
        verbose_name='Article'
        
