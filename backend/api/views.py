from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import TvInfoSerializer
from .models import TvInfo
from .pagination import CustomTvInfoPagination


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
        return Response({name: TvInfo.objects.order_by(name).values_list(name, flat=True).distinct()})


class RetrieveByNameView(viewsets.ModelViewSet):
    serializer_class = TvInfoSerializer

    def get_queryset(self):
        if self.kwargs['filter'] == 'country':
            infos = TvInfo.objects.filter(country__iexact=self.kwargs['name'])
        elif self.kwargs['filter'] == 'category':
            infos = TvInfo.objects.filter(category__iexact=self.kwargs['name'])
        else:
            infos = TvInfo.objects.filter(language__iexact=self.kwargs['name'])
        return infos
