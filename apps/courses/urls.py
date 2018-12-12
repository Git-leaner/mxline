# _*_ coding:utf-8 _*_ 
__author__ = 'levi'
__date__ = '2018/12/12 21:48'

from django.conf.urls import url, include

from .views import CourseListView

urlpatterns = [
    # 课程列表页
    url(r'^list',CourseListView.as_view, name="course_list"),

]