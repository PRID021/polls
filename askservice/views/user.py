# ViewSets define the view behavior.

from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from askservice.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
