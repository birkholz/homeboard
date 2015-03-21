from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        memberships = Member.objects.filter(user=user)
        return Home.objects.filter(
            Q(manager=user) | Q(member__in=memberships)
        ).distinct()

    def create(self, request, *args, **kwargs):
        data = request.data
        data['manager'] = request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MemberViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (HomeManagerPermission, permissions.IsAuthenticated)
