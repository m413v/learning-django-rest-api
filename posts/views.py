from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostRetrieveSerializer, PostCreateSerializer

from rest_framework.permissions import IsAdminUser, IsAuthenticated
# Create your views here.

class PostViewSet(ModelViewSet):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    # permission_classes = [IsAdminUser]

    def get_permissions(self):
        #print(self.action)
        if self.action in {'list', 'retrieve'}:
            return []

        return [IsAdminUser()]

    def get_serializer_class(self):
        if self.action in {'list', 'retrieve'}:
            return PostRetrieveSerializer
        return PostCreateSerializer

