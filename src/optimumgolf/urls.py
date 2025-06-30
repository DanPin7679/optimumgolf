from django.contrib import admin
from django.urls import path

from . import views
from players.views import player_list

urlpatterns = [
    path('', views.home),
    path('players', player_list),
    path('healthz/', views.healthz_view),
    path('admin/', admin.site.urls),
]