from rest_framework import routers
from api.views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    UserViewSet,
    FollowViewSet)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts'),
router.register(r'groups', GroupViewSet, basename='groups'),
router.register(r'users', UserViewSet),
router.register(r'follow', FollowViewSet, basename='follows'),
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
