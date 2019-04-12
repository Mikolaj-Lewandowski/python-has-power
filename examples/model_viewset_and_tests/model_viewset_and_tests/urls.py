from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chess import views
from chess.chess_match_resource import ChessMatchResource
from chess.chess_player_resource import ChessPlayerResource

router = DefaultRouter()
router.register(r'chess-player-resource', ChessPlayerResource)
router.register(r'chess-match-resource', ChessMatchResource)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chess/', views.index),
    path('chess/', include(router.urls)),
]
