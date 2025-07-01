from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

#from .models import Player


def dashboard(request):
    #player_list = Player.objects.all
    template = loader.get_template("assessments/dashboard.html")
    context = {}
    return HttpResponse(template.render(context, request))
