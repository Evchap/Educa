# from django.conf.urls import url
from django.urls import re_path
from django.urls import re_path as url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^subjects/$', views.SubjectListView.as_view(), name='subject_list'), # iss17
    url(r'^subjects/(?P<pk>\d+)/$', views.SubjectDetailView.as_view(), name='subject_detail'),# iss17
    url(r'^courses/(?P<pk>\d+)/enroll/$', views.CourseEnrollView.as_view(), name='course_enroll'), # iss18

]
