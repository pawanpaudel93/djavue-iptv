from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, UserProfileDetailView, UserFavouritesView, UserFavouritesListView

urlpatterns = [
    #gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile", UserProfileDetailView.as_view(), name="profile"),
    path("favourites/", UserFavouritesView.as_view(), name="favourites"),
    path("favourites/ids/", UserFavouritesListView.as_view(), name="favourites-ids"),
]