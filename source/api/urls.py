from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'like', LikeViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls))
]




