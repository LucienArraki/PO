from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Create your views here.

def post_list(request):
    oferta = Oferta.objects.order_by('idO')
    skladniki = Skladniki
    return render(request, 'RedPepper/index.html', {'oferta': oferta, 'skladniki': skladniki})


def order(request):
    oferta = Oferta.objects.order_by('idO')
    skladniki = Skladniki
    return render(request, 'RedPepper/zamowienie.html', {'oferta': oferta, 'skladniki': skladniki})


def pay(request):
    oferta = Oferta.objects.order_by('idO')
    skladniki = Skladniki
    return render(request, 'RedPepper/platnosc.html', {'oferta': oferta, 'skladniki': skladniki})


@csrf_exempt
def addPOST(request):
    if request.method == "POST":
        try:
            zamowienie = Zamówienie()
            zamowienie.klient.add(request.POST.get("login"))
            zamowienie.zamowienia.add(request.POST.get("zamowienie"))
            zamowienie.Platnosc.add(request.POST.get("platnosc"))
            zamowienie.save()
        except KeyError:
            return render(request, 'polls/detail.html', {
                'error_message': "You didn't select a choice.",
            })
    return HttpResponse()
