from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Course


def course_list(request):
    course_list = Course.objects.all
    template = loader.get_template("courses/list.html")
    context = {"courses": course_list}
    return HttpResponse(template.render(context, request))

