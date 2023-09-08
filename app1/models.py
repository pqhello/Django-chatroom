from django.db import models

# Create your models here.

# class Qq_andpassword(models.Model):
#     # QQ号纯数字
#     qqid = models.CharField(max_length=15,verbose_name='QQ号',primary_key=True)
#     # 密码至少6位
#     password = models.CharField(max_length=15,verbose_name='密码')
class Chat(models.Model):
    sender = models.ForeignKey('Userinfo', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    room_id = models.CharField(max_length=15,default='1')#聊天室,公共聊天室是1，两人聊天时，是被发送对象的qqid

class Userinfo(models.Model):
    #QQ号
    qqid = models.CharField(max_length=15,verbose_name='QQ号',primary_key=True)
    # 密码至少6位
    password = models.CharField(max_length=15, verbose_name='密码',default='123456')
    #昵称
    username = models.CharField(max_length=10,verbose_name="昵称")
    #性别
    gender = models.CharField(max_length=1,verbose_name="性别")
    #年龄
    age = models.IntegerField(verbose_name="年龄")

class Friend_relation(models.Model):
    qqid = models.CharField(max_length=15,verbose_name='QQ号')
    qqid_friend = models.CharField(max_length=15,verbose_name='QQ号')
    class Meta:
        unique_together = (("qqid_friend", "qqid"),)
