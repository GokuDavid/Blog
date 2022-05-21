from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    body_html=serializers.SerializerMethodField()
    toc_html=serializers.SerializerMethodField()

    def get_body_html(self,obj):
        return obj.get_md()[0]

    def get_toc_html(self,obj):
        return obj.get_md()[1]
    class Meta:
        model=Article
        fields='__all__'
        