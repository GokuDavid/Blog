from django.shortcuts import render

# Create your views here.
from article.models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer
from django.http import Http404

class ArticleList(APIView):
    def get(self,request,format=None):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(request.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
