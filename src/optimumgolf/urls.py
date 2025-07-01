from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthz/', views.healthz_view),

    path('', views.home),
    path("players/", include("players.urls")),
    path("stats/", include("stats.urls")),
    path("courses/", include("courses.urls")),
    
    
]