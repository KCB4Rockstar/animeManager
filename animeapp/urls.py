from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landingPage,name = "anime_full"),
    url(r'^catalog/$', views.viewAnimes.as_view(),name = "anime_full_view"),
    url(r'^add/$', views.addAnime,name = "add_anime"),
    url(r'^edit/$', views.editAnime,name = "edit_anime"),
    url(r'^delete/$', views.deleteAnime,name = "delete_anime"),
    url(r'^test/$', views.test,name = "test"),
    url(r'^data/refresh/$', views.readCSVtoDatabase,name = "readCSVtoDatabase"),
    url(r'^table/$', views.loadTablePage,name = "test"),
    url(r'^ajax/loadTable/$', views.loadTable, name='loadTable'),
]