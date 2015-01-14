from rest_framework import serializers
from chores.models import Chore, Assignment


class ChoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chore


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment