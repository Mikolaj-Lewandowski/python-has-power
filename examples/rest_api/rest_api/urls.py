from django.contrib import admin
from django.urls import path

from chess import views
from chess.chess_player_resource import ChessPlayerResource

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chess/', views.index),
    path('chess/chess-player-resource/', ChessPlayerResource.as_view()),
    path('chess/chess-player-resource/<int:pk>/', ChessPlayerResource.as_view()),
]
