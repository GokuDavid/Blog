from django.shortcuts import render
from article.models import Article
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.pagination import CommonPageNumberPagination
from .serializers import ArticleSerializer
from django.http import Http404
from .permissions import IsAdminUserOrReadOnly


class ArticleList(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, format=None):
        articles = Article.objects.all()
        paginator = CommonPageNumberPagination()
        res = paginator.paginate_queryset(articles, request, self)
        serializer = ArticleSerializer(res, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
