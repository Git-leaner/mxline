from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.shortcuts import render


class CourseListView(View):
    def get(self,request):
        return render(request,'course-list.html',{})