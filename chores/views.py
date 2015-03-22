from rest_framework import viewsets

from chores.models import Chore, Assignment
from chores.serializers import ChoreSerializer, AssignmentSerializer


class ChoreViewSet(viewsets.ModelViewSet):
    queryset = Chore.objects.all()
    serializer_class = ChoreSerializer

    def get_queryset(self):
        queryset = Chore.objects.all()
        home = self.request.QUERY_PARAMS.get('home', None)
        if home:
            queryset = queryset.filter(home__id=home)
        return queryset


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
