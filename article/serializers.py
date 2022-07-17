from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer


class ArticleSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="article:detail")
    # author = UserDescSerializer(read_only=True)

    # body_html = serializers.SerializerMethodField()
    # toc_html = serializers.SerializerMethodField()


    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'
