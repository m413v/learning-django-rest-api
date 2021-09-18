from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostRetrieveSerializer, PostCreateSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# Create your views here.
from rest_framework.response import Response



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

    def create(self, request, *args, **kwargs):
        request.data.update({'author': request.user.pk})
        serializer = self.get_serializer(data=request.data, author=request.user)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
