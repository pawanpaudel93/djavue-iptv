from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.db.models import Count, F
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.utils import IntegrityError
from m3u_parser import M3uParser

from .serializers import TvInfoSerializer
from .permissions import IsOwnerOrReadOnly
from .models import TvInfo
from .pagination import CustomTvInfoPagination
from backend.accounts.models import UserProfile


class PlayerView(TemplateView):
    template_name='api/player.html'

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        url = self.request.GET['url']
        context = super(PlayerView, self).get_context_data(**kwargs)
        context["url"] = url
        return context
    

class ListTvInfoView(viewsets.ModelViewSet):
    serializer_class = TvInfoSerializer
    pagination_class = CustomTvInfoPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        infos = TvInfo.objects.filter(user=None).order_by(self.kwargs['order'])
        return infos


class ListTitlesView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        data = {
            name: TvInfo.objects.filter(user=None).annotate(key=F(name)).order_by('key').values('key').annotate(counts=Count('id'))
        }
        return Response(data)


class RetrieveByNameView(viewsets.ModelViewSet):
    serializer_class = TvInfoSerializer
    pagination_class = CustomTvInfoPagination
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.kwargs['filter'] == 'country':
            infos = TvInfo.objects.filter(country__iexact=self.kwargs['name'], user=None)
        elif self.kwargs['filter'] == 'category':
            infos = TvInfo.objects.filter(category__iexact=self.kwargs['name'], user=None)
        elif self.kwargs['filter'] == 'language':
            infos = TvInfo.objects.filter(language__iexact=self.kwargs['name'], user=None)
        else:
            infos = TvInfo.objects.filter(user=None).all()
        return infos


class ParseM3uView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.FILES:
            file_path = request.FILES['file'].file.name
            file = M3uParser()
            file.parse_m3u(file_path)
            tv_infos = file.get_list()
            return Response(tv_infos)
        else:
            return Response({"Error": "No file uploaded!"})
    
    def get(self, request, *args, **kwargs):
        file_path = request.GET['url']
        if file_path:
            file = M3uParser()
            file.parse_m3u(file_path)
            tv_infos = file.get_list()
            return Response(tv_infos, status=status.HTTP_200_OK)
        else:
            return Response({"Error": "No file Found!"}, status=status.HTTP_404_NOT_FOUND)


class TvInfoListCreateView(generics.ListCreateAPIView):
    queryset = TvInfo.objects.all()
    serializer_class = TvInfoSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomTvInfoPagination

    def get_queryset(self):
        return TvInfo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        try:
            return super(generics.ListCreateAPIView, self).create(request, *args, **kwargs)
        except IntegrityError:
            content = {'error': 'IntegrityError'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FavUnfavChannelsView(APIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        channel_id = data.get("channel_id", None)
        action = data.get("action", None)
        channel = TvInfo.objects.filter(id=channel_id).first()
        user_profile = UserProfile.objects.get(user=request.user)
        if action and action == "fav" and channel:
            if not channel.userprofile_set.filter(pk=user_profile.pk).exists():
                user_profile.channels.add(channel)
                response = Response({
                    "status": "success",
                    "description": f"{channel_id} is added to favourites."
                })
            else:
                response = Response({
                    "status": "present",
                    "description": f"Channel {channel_id} is already in favourites."
                })
        elif action and action == "unfav" and channel:
            if channel.userprofile_set.filter(pk=user_profile.pk).exists():
                user_profile.channels.remove(channel)
                response = Response({
                    "status": "success",
                    "description": f"Channel {channel_id} is removed from favourites."
                })
            else:
                response = Response({
                    "status": "absent",
                    "description": f"Channel {channel_id} is not in favourites."
                })
        else:
            response = Response(
                {   
                    "status": "failure",
                    "description": "action or channel_id missing",
                    "action": action if action else "absent",
                    "channel_id": channel_id if channel_id else "absent"
            })
        return response
