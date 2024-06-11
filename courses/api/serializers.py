from rest_framework import serializers

from .permissions import ModuleWithContentsSerializer
from ..models import Subject
# from .serializers import UserSerializer, GroupSerializer

class SubjectSerializer(serializers.ModelSerializer): # iss14
    class Meta:
        model = Subject
        fields = ('id', 'title', 'slug')


from ..models import Course


# class CourseSerializer(serializers.ModelSerializer): # iss18
#     class Meta:
#         model = Course
#         fields = ('id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules')


from rest_framework import serializers
from ..models import Course, Module


class ModuleSerializer(serializers.ModelSerializer): # iss18
    order = serializers.CharField(required=False) # подсказка из интернета
    class Meta:
        model = Module
        fields = ('order', 'title', 'description')

# class CourseSerializer(serializers.ModelSerializer): # iss18
#     class Meta:
#         model = Course
#         fields = ('id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules')

class CourseSerializer(serializers.ModelSerializer): # iss18
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules')


class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner', 'modules']