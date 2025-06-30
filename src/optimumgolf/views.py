from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

PROJECT_NAME = getattr(settings, "PROJECT_NAME", "Unset Project in Views")

def hello_world(request):
    return render(request, "hello-world.html", {
        "project_name": "Optimum Golf"
    })


def healthz_view(request):
    return HttpResponse("OK")