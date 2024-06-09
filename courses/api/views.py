from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class SubjectListView(generics.ListAPIView): # iss17
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView): # iss17
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Course


class CourseEnrollView(APIView): # iss19
    authentication_classes = (BasicAuthentication,)  # iss20
    permission_classes = (IsAuthenticated,) # iss21

    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})


from rest_framework import viewsets
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet): #iss22
    queryset = Course.objects.all() #iss22
    serializer_class = CourseSerializer #iss22
