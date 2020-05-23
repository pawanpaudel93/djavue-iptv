from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.db.models import Count, F

from .serializers import TvInfoSerializer
from .models import TvInfo
from .pagination import CustomTvInfoPagination
from .m3uParser import M3uParser


class ListTvInfoView(viewsets.ModelViewSet):
    serializer_class = TvInfoSerializer
    pagination_class = CustomTvInfoPagination

    def get_queryset(self):
        infos = TvInfo.objects.order_by(self.kwargs['order'])
        return infos


class ListTitlesView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        data = {
            name: TvInfo.objects.annotate(key=F(name)).order_by('key').values('key').annotate(counts=Count('id'))
        }
        return Response(data)


class RetrieveByNameView(viewsets.ModelViewSet):
    serializer_class = TvInfoSerializer
    pagination_class = CustomTvInfoPagination

    def get_queryset(self):
        if self.kwargs['filter'] == 'country':
            infos = TvInfo.objects.filter(country__iexact=self.kwargs['name'])
        elif self.kwargs['filter'] == 'category':
            infos = TvInfo.objects.filter(category__iexact=self.kwargs['name'])
        elif self.kwargs['filter'] == 'language':
            infos = TvInfo.objects.filter(language__iexact=self.kwargs['name'])
        else:
            infos = TvInfo.objects.all()
        return infos


class ParseM3uView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        file_path = request.FILES['file'].file.name
        file = M3uParser()
        file.parse_m3u(file_path)
        tv_infos = file.get_dict()
        return Response(tv_infos)
