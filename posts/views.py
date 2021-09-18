from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import  PostSerializer


# Create your views here.

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = [IsAdminUser]
