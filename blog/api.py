from rest_framework.routers import DefaultRouter

from users.views import UserViewSet
from posts.views import PostViewSet


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)

