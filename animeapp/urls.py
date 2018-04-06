from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.landingPage,name = "anime_full"),
    url(r'^catalog/$', views.viewAnimesByCreated.as_view(),name = "anime_created_view"),
    url(r'^catalog/add/$', views.addAnime,name = "add_anime"),
    path('catalog/anime/<uuid:animeID>/edit/', views.editAnime,name = "edit_anime"),
    path('catalog/anime/<uuid:animeID>/delete/', views.deleteAnime,name = "delete_anime"),
    url(r'^catalog/sort/name', views.viewAnimesByName.as_view(),name = "anime_name_view"),
    url(r'^catalog/sort/type', views.viewAnimesByType.as_view(),name = "anime_type_view"),
    url(r'^catalog/sort/episodes', views.viewAnimesByNumEpisodes.as_view(),name = "anime_episode_view"),
    url(r'^catalog/sort/members', views.viewAnimesByNumMembers.as_view(),name = "anime_members_view"),
    url(r'^catalog/sort/rating', views.viewAnimesByRating.as_view(),name = "anime_rating_view"),
    path('catalog/anime/<uuid:animeID>/', views.singlePage, name='anime-detail'),
    url(r'^adminsettings/$', views.adminSettings,name = "admin_settings"),
    url(r'^data/refresh/$', views.readCSVtoDatabase,name = "readCSVtoDatabase"),
    url(r'^data/images/$', views.loadImages,name = "retrieveImages"),
    url(r'^data/clear/$', views.clearDatabase,name = "clear_database"),
    url(r'^table/$', views.loadTablePage,name = "viewCSV"),
    url(r'^ajax/loadTable/$', views.loadTable, name='loadTable'),
    url(r'^access_denied/$', views.accessDenied,name = "accessDenied"),
]