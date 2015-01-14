from django.contrib.auth.models import User
from rest_framework import viewsets
from home.models import Home, Member
from home.serializers import UserSerializer, HomeSerializer, MemberSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows homes to be viewed or edited.
    """
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer