from django.contrib.auth.models import User
from rest_framework import serializers
from home.models import Home, Member


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class HomeSerializer(serializers.ModelSerializer):
    is_manager = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = ('id', 'title', 'manager', 'members', 'is_manager')

    def get_is_manager(self, obj):
        request = self.context.get('request', None)
        if request is not None:
            return obj.manager == request.user
        return False

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member