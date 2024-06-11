from rest_framework.permissions import BasePermission

# class IsEnrolled(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.students.filter(id=request.user.id).exists()

from rest_framework import serializers
from rest_framework.permissions import BasePermission # iss24


class IsEnrolled(BasePermission): # iss24
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()

from ..models import Content, Module, Course  # iss25


class ItemRelatedField(serializers.RelatedField): # iss25
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer): # iss25
    order = ItemRelatedField(read_only=True)
    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ('order', 'item')

class ModuleWithContentsSerializer(serializers.ModelSerializer): # iss25
    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = ('order', 'title', 'description', 'contents')


class CourseWithContentsSerializer(serializers.ModelSerializer): # iss25
    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules')
