from rest_framework import viewsets

from chores.models import Chore, Assignment
from chores.serializers import ChoreSerializer, AssignmentSerializer


class ChoreViewSet(viewsets.ModelViewSet):
    queryset = Chore.objects.all()
    serializer_class = ChoreSerializer

    def get_queryset(self):
        home = self.request.QUERY_PARAMS.get('home', None)
        completed = self.request.QUERY_PARAMS.get('completed', False)
        if home and completed:
            return Chore.objects.filter(home__id=home, completed__isnull=False)
        elif home:
            return Chore.objects.filter(home__id=home, completed__isnull=True)
        return Chore.objects.all()


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
