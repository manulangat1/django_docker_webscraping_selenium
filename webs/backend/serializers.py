from rest_framework import serializers


from .models import Articles,Records

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'id',
            'title',
            'post',
            'user',
            'comments',
            'scrap_date'
        )

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'id',
            'start_time',
            'success',
            'scrap_date'
        )