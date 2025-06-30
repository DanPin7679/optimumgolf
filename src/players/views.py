from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Player


def player_list(request):
    player_list = Player.objects.all
    template = loader.get_template("players/list.html")
    context = {"players": player_list}
    return HttpResponse(template.render(context, request))

