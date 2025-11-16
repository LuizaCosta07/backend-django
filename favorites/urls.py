from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet

router = DefaultRouter()
router.register(r'', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:movie_id>/add/', FavoriteViewSet.as_view({'post': 'add_favorite'}), name='add-favorite'),
    path('<int:movie_id>/remove/', FavoriteViewSet.as_view({'delete': 'remove_favorite'}), name='remove-favorite'),
]
