from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
...
# Create your views here.
def show_mywatchlist(request):
    data_film_mywatchlist = MyWatchList.objects.all()
    context = {
    'list_movie': data_film_mywatchlist,
    'nama': 'Abdillah Sulthan Naufal Panggabean',
    'npm' : '2106637555',
    'info':''
    }
    jumlah_film = 0

    for film in data_film_mywatchlist:
        if film.watched == "Sudah":
            jumlah_film += 1
    
    if jumlah_film >= (len(data_film_mywatchlist)/2):
        context["info"] += "Selamat, kamu sudah banyak menonton!"
    
    else:
        context["info"] += "Wah, kamu masih sedikit menonton!"
    
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")