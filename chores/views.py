from rest_framework import viewsets
from chores.models import Chore, Assignment
from chores.serializers import ChoreSerializer, AssignmentSerializer


class ChoreViewSet(viewsets.ModelViewSet):
    queryset = Chore.objects.all()
    serializer_class = ChoreSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
