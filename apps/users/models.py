# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser,UserManager,PermissionsMixin,BaseUserManager
from uuid import uuid4

class BaseSetting(object):
    enable_themes=True
    use_bootwatch=True

class GlobalSetting(object):
    site_title = "后台管理系统"
    site_footer="在线管理"
    menu_style="accordion"

class CustomUserManager(BaseUserManager):
    def create_user(self, username,first_name,last_name, email, password=None ):
        now = datetime.now()
        if not email:
            raise ValueError('The email is required to create this user')
        email = CustomUserManager.normalize_email(email)
        cuser = self.model(email=email,is_staff=False,username=username,first_name=first_name,last_name=last_name,
                           is_active=True, is_superuser=False,
                           date_joined=now, last_login=now, )
        cuser.set_password(password)
        cuser.save(using=self._db)
        return cuser

    def create_superuser(self,username,first_name,last_name, email, password=None ):
        u = self.create_user(username,first_name,last_name, email,  password )
        u.id=uuid4()
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u
class UserProfile(AbstractBaseUser,PermissionsMixin):
    id = models.CharField(unique=True,default="",max_length=50)
    username = models.CharField(primary_key=True,max_length=30,verbose_name=u"用户名",default="")
    first_name = models.CharField(verbose_name=u'first name', max_length=45)
    last_name = models.CharField(verbose_name=u'last name', max_length=45)
    nick_name=models.CharField(max_length=50, verbose_name=u"昵称",default="")
    birthday=models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender=models.CharField(max_length=6,choices=(("male",u"男"),("female","女")),default="")
    address=models.CharField(max_length=100, default=u"")
    mobile=models.CharField(max_length=11, null=True, blank=True)
    image=models.ImageField(upload_to="image/&Y/%m",default=u"image/default.png",max_length=100)
    #  type object 'UserProfile' has no attribute 'USERNAME_FIELD'
    # identifier = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=50, verbose_name=u"邮箱",default="")
    # email=models.ForeignKey(Ema,verbose_name=u"邮箱",on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=('date joined'), default=datetime.now)
    object=CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']
    # Default Permission
    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username

    # @property
    # def is_superuser(self):
    #     return self.is_admin
    # @property
    # def is_staff(self):
    #     return self.is_admin
    # @property
    # def is_superuser_property(self):
    #     return self.is_admin

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    # email=models.ForeignKey(UserProfile,verbose_name=u"邮箱",on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, verbose_name=u"邮箱",default="")
    send_type = models.CharField(verbose_name=u"验证码类型",choices=(("register", u"注册"), ("forget", u"找回密码"), ("update_email", u"修改邮箱")),
                                 max_length=30)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

class Banner(models.Model):
    title=models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图")
    url=models.URLField(max_length=200, verbose_name=u"访问地址")
    index =models.IntegerField(default=100,verbose_name=u"顺序")
    add_time=models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural=verbose_name