from rest_framework import generics
from ..models import Subject, Course
from .serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView): # iss17
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView): # iss17
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

from rest_framework import viewsets
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet): #iss22
    queryset = Course.objects.all() #iss22
    serializer_class = CourseSerializer #iss22
