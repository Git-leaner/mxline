from __future__ import unicode_literals
from django.db import models
from datetime import  datetime
# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=50, verbose_name=u"课程名")
    desc=models.CharField(max_length=300, verbose_name=u"课程描述")
    detail=models.CharField(max_length=50, verbose_name=u"课程详情")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    degree=models.CharField(choices=(("cj","初级"),("zj","中级"),("gj","高级")), verbose_name=u"课程名",max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students=models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_numbers=models.IntegerField(default=0, verbose_name=u"收藏人数")
    image=models.ImageField(upload_to="courses/&Y/%m",verbose_name=u"封面图",max_length=100)
    click_nums=models.IntegerField(default=0, verbose_name=u"点击数")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name=u"课程"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程名",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    #     return self.name
    #
    # def get_lesson_video(self):
    #     #获取章节视频
    #     return self.video_set.all()

class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    #     return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name