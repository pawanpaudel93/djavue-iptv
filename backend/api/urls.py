from django.urls import path, re_path
from .views import ListTvInfoView, ListTitlesView, RetrieveByNameView, ParseM3uView

urlpatterns = [
    path('iptv/<slug:order>/', ListTvInfoView.as_view({'get': 'list'}), name="alltvinfos"),
    path('iptv/titles/<slug:name>/', ListTitlesView.as_view(), name="titles"),
    re_path(r"^iptv/channels/(?P<filter>.*)/(?P<name>.*)/$", RetrieveByNameView.as_view({'get': 'list'}), name="retrieve"),
    path('parsem3u', ParseM3uView.as_view(), name='parsem3u')
]

