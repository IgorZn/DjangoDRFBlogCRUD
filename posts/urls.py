from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet
# from .views import PostList, PostDetail, UserList, UserDetail

router = SimpleRouter()

# the order of routers is sensitive
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]