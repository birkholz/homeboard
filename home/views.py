from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAdminUser
from home.models import Home, Member
from home.permissions import HomeManagerPermission
from home.serializers import UserSerializer, HomeSerializer, MemberSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class HomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows homes to be viewed or edited.
    """
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MemberViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (HomeManagerPermission, permissions.IsAuthenticated)
