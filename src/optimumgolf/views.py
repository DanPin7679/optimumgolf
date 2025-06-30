from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})

def healthz_view(request):
    return HttpResponse("OK")