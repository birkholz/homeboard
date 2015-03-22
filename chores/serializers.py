from rest_framework import serializers
from chores.models import Chore, Assignment


class ChoreSerializer(serializers.ModelSerializer):
    is_assigned = serializers.SerializerMethodField()
    class Meta:
        model = Chore
        fields = ('title', 'description', 'assigned_to', 'is_assigned', 'home', 'id', 'completed')

    def get_is_assigned(self, obj):
        request = self.context.get('request', None)
        if request is not None:
            try:
                Assignment.objects.get(chore=obj, user=request.user)
                return True
            except Assignment.DoesNotExist:
                return False
        return False


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment