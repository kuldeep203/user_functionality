from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['incident_id', 'details', 'priority', 'status', 'created_at', 'enterprise_or_government', 'reporter']
        read_only_fields = ['incident_id', 'created_at']

    def validate(self, data):
        """
        Ensure the reporter is automatically set to the logged-in user.
        """
        user = self.context['request'].user
        if 'reporter' not in data:  # Automatically assign the logged-in user as the reporter
            data['reporter'] = user
        return data

    def validate_status(self, value):
        """
        Ensure that closed incidents cannot be edited.
        """
        if self.instance and self.instance.status == 'Closed' and value != self.instance.status:
            raise serializers.ValidationError("Closed incidents cannot be edited.")
        return value
