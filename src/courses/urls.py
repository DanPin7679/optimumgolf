from django.urls import path

from . import views


urlpatterns = [
    path("<slug:course_id>/lessons/<slug:lesson_id>/", views.lesson_detail),
    path("<slug:course_id>/", views.course_detail),
    path("", views.course_list),
]