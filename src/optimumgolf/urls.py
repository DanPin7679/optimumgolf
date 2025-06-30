from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('', views.home),
    path("players/", include("players.urls")),
    path("stats/", include("stats.urls")),
    path('healthz/', views.healthz_view),
    path('admin/', admin.site.urls),
]