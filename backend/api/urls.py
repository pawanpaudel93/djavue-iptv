from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('iptv/channels/', TvInfoListCreateView.as_view(), name="tvinfos"),
    path('iptv/channels/<int:pk>', TvInfoRetrieveUpdateDestroyView.as_view(), name="tvinfos-rud"),
    path('iptv/<slug:order>/', ListTvInfoView.as_view({'get': 'list'}), name="alltvinfos"),
    path('iptv/titles/<slug:name>/', ListTitlesView.as_view(), name="titles"),
    path("iptv/fav-unfav", FavUnfavChannelsView.as_view(), name="fav_unfav"),
    re_path(r"^iptv/channels/(?P<filter>.*)/(?P<name>.*)/$", RetrieveByNameView.as_view({'get': 'list'}), name="retrieve"),
    path('parsem3u', ParseM3uView.as_view(), name='parsem3u'),
]

