
from django.http import HttpResponse
from django.shortcuts import render


def player_list(request):
    return render(request, "players/list.html", {
        "players": [
            {"name": "Cedric", "dexterity": "right"},
            {"name": "Zach", "dexterity": "right"}
        ]
    })
