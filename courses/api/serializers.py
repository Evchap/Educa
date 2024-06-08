from rest_framework import serializers
from ..models import Subject


class SubjectSerializer(serializers.ModelSerializer): # iss14
    class Meta:
        model = Subject
        fields = ('id', 'title', 'slug')
