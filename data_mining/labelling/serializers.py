from rest_framework import serializers

from .models import Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = (
            'id', 'line', 'option1', 'option2', 'option3', 'option4', 'resulf', 'content', 'is_good'
        )
