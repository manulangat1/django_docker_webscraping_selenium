# from rest_framework import generics
# from rest_framework.response import Response

# from .models import Records,Articles
# from .serializers import ArticleSerializer,RecordsSerializer


# class ArticleListView(generics.ListAPIView):
#     serializer_class = ArticleSerializer
#     queryset = Articles.objects.all()

# class ArticleDetailView(generics.RetrieveAPIView):
#     serializer_class = ArticleSerializer
#     queryset = Articles.objects.all()

# class RecordListView(generics.ListAPIView):
#     serializer_class = RecordsSerializer
#     queryset = Records.objects.all()

# class RecordDetailView(generics.RetrieveAPIView):
#     serializer_class = RecordsSerializer
#     queryset = Records.objects.all()