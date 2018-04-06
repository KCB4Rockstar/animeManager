from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
import os
import re
import json
import urllib
import csv
from . models import Anime
from .animes import AddAnime, Anime
from csv import reader
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#from django.contrib.auth.models import User
#from django.core.files import File

# Create your views here.


def landingPage(request):
    return render(request, 'animes/landing.html')

class viewAnimesByCreated(generic.ListView):
    model = Anime
    paginate_by = 48
    context_object_name = 'animes'
    ordering = ['-created']
    template_name = 'animes/all.html'

class viewAnimesByName(generic.ListView):
    model = Anime
    paginate_by = 48
    context_object_name = 'animes'
    ordering = ['name']
    template_name = 'animes/all.html'

class viewAnimesByType(generic.ListView):
    model = Anime
    paginate_by = 48
    context_object_name = 'animes'
    ordering = ['animeType']
    template_name = 'animes/all.html'

class viewAnimesByNumEpisodes(generic.ListView):
    model = Anime
    paginate_by = 48
    context_object_name = 'animes'
    ordering = ['-episodes']
    template_name = 'animes/all.html'

class viewAnimesByNumMembers(generic.ListView):
    model = Anime
    paginate_by = 48
    context_object_name = 'animes'
    ordering = ['-members']
    template_name = 'animes/all.html'

class viewAnimesByRating(generic.ListView):
    model = Anime
    paginate_by = 48
    context_object_name = 'animes'
    ordering = ['-rating']
    template_name = 'animes/all.html'

def readCSVtoDatabase(request):
    def isFloat(n):
        try:
            float(n)
            return True
        except ValueError:
            return False

    numAnimes = Anime.objects.all().count()

    if(numAnimes==0):
        fp = open(os.path.join(settings.MEDIA_ROOT, 'anime.csv'))
        data = fp.read()
        raw_record_row = []
        raw_record_row = data.split("\n")
        fp.close()
        records = []
        for val in reader(raw_record_row, dialect=csv.excel):
            records.append(val)
        #for i in range(1, len(records)):
        for i in range(1, 100):
            if(len(records[i])==7):
                if(records[i][2]==""):
                    g = "Unknown"
                else:
                    g = records[i][2]
                if(records[i][3]==""):
                    t = "Unknown"
                else:
                    t = records[i][3]
                if(records[i][4].isdigit()):
                    eps = int(records[i][4])
                else:
                    eps = -1
                
                if isFloat(records[i][5]):
                    rate = float(records[i][5])
                else:
                    rate = -1

                if(records[i][6].isdigit()):
                    mems = int(records[i][6])
                else:
                    mems = -1
                obj = Anime.objects.create(name=records[i][1].replace("&#039;","'"), genre=g, animeType=t, episodes=eps, rating=rate, members=mems)
                obj.save()

    else:
        print("Database already loaded.")
    return HttpResponseRedirect("/catalog/")

def loadImages(request):
    queryAnimes = Anime.objects.all()
    animes = []
    for i in queryAnimes:
        animes.append(i)
    
    for i in range(0, len(animes)):
        if animes[i].photoCover == "":
            try:
                obj = Anime.objects.get(id = animes[i].id)
                searchName = re.sub('[^A-Za-z0-9]+', '', obj.name)
                searchName = searchName.split()
                searchName='+'.join(searchName)
                url = "http://www.google.com/search?q="+searchName+"+myanimelist"+"&tbm=isch"
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                
                htmlText = BeautifulSoup(urlopen(Request(url,headers=headers)),'html.parser')
                img = htmlText.find("div",{"class":"rg_meta"})
                imgURL = json.loads(img.text)["ou"]
                obj.photoCover = imgURL
            except:
                obj.photoCover = ""
            obj.save()

    return HttpResponseRedirect("/adminsettings/")

def clearDatabase(request):
    if Anime.objects.all().count() > 0:
        Anime.objects.all().delete()
    return HttpResponseRedirect("/adminsettings/")

def loadTablePage(request):
    if request.user.is_authenticated:
        return render(request, 'animes/table.html')
    else:
        return HttpResponseRedirect("/access_denied/")

def loadTable(request):
    if request.user.is_authenticated:
        fp = open(os.path.join(settings.MEDIA_ROOT, 'anime.csv'))
        data = fp.read()
        fp.close()
        
        req = {
            'csvData': data
        }
        return JsonResponse(req)
    else:
        return HttpResponseRedirect("/access_denied/")

def singlePage(request, animeID):
    result = Anime.objects.get(id = animeID)
    return render(request, "animes/singleAnime.html", {
        "anime": result
    })

def addAnime(request):
    if request.user.is_authenticated:
        add_form = AddAnime()
        if request.method == "POST":
            add_form = AddAnime(request.POST, request.FILES)

            if add_form.is_valid():
                anime = Anime()
                anime.name = add_form.cleaned_data['name']
                anime.genre = add_form.cleaned_data['genre']
                anime.animeType = add_form.cleaned_data['animeType']
                anime.episodes = add_form.cleaned_data['episodes']
                anime.rating = add_form.cleaned_data['rating']
                anime.members = add_form.cleaned_data['members']
                print(add_form.cleaned_data['photoCover'])
                anime.photoCover = add_form.cleaned_data['photoCover']

                add_form.save()
                return HttpResponseRedirect("/")

        else:
            return render(request, 'animes/add.html', {
                'add_form': add_form
            })
    else:
        return HttpResponseRedirect("/access_denied/")

def editAnime(request, animeID):
    if request.user.is_authenticated:
        update_form = AddAnime()
        result = Anime.objects.get(id = animeID)

        if request.method == "POST":
            update_form = AddAnime(request.POST, request.FILES)
            if update_form.is_valid():
                result.name = update_form.cleaned_data['name']
                result.genre = update_form.cleaned_data['genre']
                result.animeType = update_form.cleaned_data['animeType']
                result.episodes = update_form.cleaned_data['episodes']
                result.rating = update_form.cleaned_data['rating']
                result.members = update_form.cleaned_data['members']
                result.photoCover = update_form.cleaned_data['photoCover']

                result.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, 'animes/edit.html', {
                    'update_form': update_form,
                    'namename': animeID
            })
    else:
        return HttpResponseRedirect("/access_denied/")

def deleteAnime(request, animeID):
    if request.user.is_authenticated:
        result = Anime.objects.get(id = animeID).delete()
        return HttpResponseRedirect("/catalog/")
    else:
        return HttpResponseRedirect("/access_denied/")

def isLoggedIn(request):
    username = request.POST['username']
    password = request.POST['password']
    User = authenticate(request, username=username, password=password)

    return render(request, 'animes/all.html', {
        "animes": User
    })

def adminSettings(request):
    if request.user.is_authenticated:
        dataCount = Anime.objects.all().count()
        return render(request, 'animes/adminPage.html', {
            "data": dataCount
        })
    else:
        return render(request, 'access_denied.html')

def accessDenied(request):
    return render(request, 'access_denied.html')