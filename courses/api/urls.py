# from django.conf.urls import url
from django.urls import re_path, include
from django.urls import re_path as url
from . import views
from rest_framework import routers

app_name = 'courses'

router = routers.DefaultRouter() #iss22
router.register('courses', views.CourseViewSet) #iss22


urlpatterns = [
    url(r'^subjects/$', views.SubjectListView.as_view(), name='subject_list'), # iss17
    url(r'^subjects/(?P<pk>\d+)/$', views.SubjectDetailView.as_view(), name='subject_detail'),# iss17
    url(r'^courses/(?P<pk>\d+)/enroll/$', views.CourseEnrollView.as_view(), name='course_enroll'), # iss18
    url(r'^', include(router.urls)), #iss22

]


