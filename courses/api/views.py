from rest_framework import generics
from ..models import Subject, Course
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


# class CourseEnrollView(APIView): # iss19 # iss23 класс удален
#     authentication_classes = (BasicAuthentication,)  # iss20
#     permission_classes = (IsAuthenticated,) # iss21
#
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})


from rest_framework import viewsets
from .serializers import CourseSerializer
# from rest_framework.decorators import detail_route # iss23 устарело
from rest_framework.decorators import action
from courses.api.permissions import IsEnrolled  # iss25
from courses.api.serializers import CourseWithContentsSerializer  # iss25


class CourseViewSet(viewsets.ReadOnlyModelViewSet): #iss22
    queryset = Course.objects.all() #iss22
    serializer_class = CourseSerializer #iss22

    @action(detail=True, methods=['post'], # iss23 новый вариант
    # @detail_route(methods=['post'], # # iss23 устарело
                  serializer_class=CourseWithContentsSerializer,  # iss25
                  authentication_classes=[BasicAuthentication],
                  # permission_classes=[IsAuthenticated]) # iss23
                  permission_classes = [IsAuthenticated, IsEnrolled])  # iss25
    # def enroll(self, request, *args, **kwargs): # iss23
    #     course = self.get_object()
    #     course.students.add(request.user)
    #     return Response({'enrolled': True})

    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
