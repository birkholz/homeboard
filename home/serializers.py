from django.contrib.auth.models import User
from rest_framework import serializers
from home.models import Home, Member


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ('title', 'manager', 'members')


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member