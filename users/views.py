from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == 'me':
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=False, methods=['GET'])
    def me(self, request: Request):

        serializer = self.serializer_class(request.user)

        return Response(serializer.data)
