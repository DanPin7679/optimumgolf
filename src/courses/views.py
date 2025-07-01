import helpers
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect

from . import services

def course_list(request):
    queryset = services.get_publish_courses()
    context = {
        "courses": queryset
    }
    template_name = "courses/list.html"
    # if request.htmx:
    #     template_name = "courses/snippets/list-display.html"
    #     context['queryset'] = queryset[:3]
    return render(request, template_name, context)

def course_detail(request, course_id=None, *args, **kwarg):
    course_obj = services.get_course_detail(course_id=course_id)
    print(course_obj)
    if course_obj is None:
        raise Http404
    lessons_queryset = services.get_course_lessons(course_obj)
    print("lesson : ", lessons_queryset[0])
    context = {
        "course": course_obj,
        "lessons": lessons_queryset,
    }
    # return JsonResponse({"data": course_obj.id, 'lesson_ids': [x.path for x in lessons_queryset] })
    return render(request, "courses/detail.html", context)


def lesson_detail(request, course_id=None, lesson_id=None, *args, **kwargs):
    lesson_obj = services.get_lesson_detail(
        course_id=course_id,
        lesson_id=lesson_id
    )
    if lesson_obj is None:
        raise Http404

    template_name = "courses/lesson.html"
    context = {
        "object": lesson_obj
    }
    
    return render(request, template_name, context)