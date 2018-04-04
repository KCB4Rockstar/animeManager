from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
import os
from django.conf import settings
from . models import Anime
from .animes import Anime
from csv import reader
from django.http import JsonResponse
#from django.contrib.auth.models import User
#from bs4 import BeautifulSoup
#import urllib
#from urllib.request import Request, urlopen
#from django.core.files import File

# Create your views here.

def landingPage(request):
    return render(request, 'animes/landing.html')

def fullAnimeDatabase(request):
    allAnimes = Anime.objects.all()
    
    return render(request, 'animes/all.html', {
        "animes": allAnimes
    })

class viewAnimes(generic.ListView):
    model = Anime
    paginate_by = 48
    context_object_name = 'animes'
    ordering = ['-created']
    template_name = 'animes/all.html'

def readCSVtoDatabase(request):
    def isFloat(n):
        try:
            float(n)
            return True
        except ValueError:
            return False

    numAnimes = Anime.objects.all().count()

    print(numAnimes)

    if(numAnimes==0):
        fp = open(os.path.join(settings.MEDIA_ROOT, 'anime.csv'))
        data = fp.read()
        raw_record_row = []
        raw_record_row = data.split("\n")
        fp.close()
        records = []
        for val in reader(raw_record_row):
            records.append(val)

        #for i in range(1, len(records)-1):
        for i in range(1, 100):
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

            obj = Anime.objects.create(name=records[i][1], genre=records[i][2], animeType=records[i][3], episodes=eps, rating=rate, members=mems)
    else:
        print("Database already loaded.")
    return HttpResponseRedirect("/catalog/")


def test(request):
    # obj = Anime.objects.create(
    #     name="jpjpjwjw", genre="wdwdyuyu", animeType="TV/Series",
    #     episodes=523, rating=1.6, members=264
    # )

    # searchName = obj.name
    # searchName = searchName.replace(" ", "%20")
    # searchName = searchName.replace("-", "%2D")
    # searchName = searchName.replace("&", "%26")

    # url = "http://www.google.com/search?q="+searchName+"&tbm=isch"

    # req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    # html = urllib.request.urlopen(req)
    # soup = BeautifulSoup(html, "html.parser")

    # pic = "n"

    # img_links = soup.findAll("img", {"class":"rg_ic"})
    # for img_link in img_links:
    #     pic=pic+img_link.img['src']

    # photoCover = img_links[0].img['src']

    # photoCover = urllib.request.urlretrieve(req)
    # obj.photoCover.save(
    #     os.path.basename(self.image_url),
    #     File(open(photoCover[0]))
    # )
    return render(request, 'test.html')

def loadTablePage(request):
    return render(request, 'animes/table.html')

def loadTable(request):
    fp = open(os.path.join(settings.MEDIA_ROOT, 'anime.csv'))
    data = fp.read()
    fp.close()
    
    req = {
        'csvData': data
    }
    return JsonResponse(req)

def addAnime(request):
    return render(request, 'animes/add.html')

def editAnime(request):
    return render(request, 'animes/edit.html')

def deleteAnime(request):
    return render(request, 'animes/delete.html')

