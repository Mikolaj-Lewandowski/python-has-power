from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

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
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
