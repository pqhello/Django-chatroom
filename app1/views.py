from django.shortcuts import render
from .models import Userinfo,Friend_relation
import time
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from .models import Chat
def index(request):
    error1=''
    if request.method == "POST":
        qqid_post =request.POST.get("qqid")
        password_post = request.POST.get("password")
        quersty = Userinfo.objects.all()
        for obj in quersty:
            qqid_db =obj.qqid
            password_db = obj.password
            if qqid_db==qqid_post and password_post==password_db:
                request.session['user_id']=int(time.time())
                request.session['qqid']=qqid_db
                request.session['is_login']=True
                request.session.set_expiry(24*60*60)
                # test = request.session.get("qqid")
                # print(test)
                return redirect('person'+'/'+qqid_post)
            else:
                error1="QQ号或密码错误"
    return render(request, "app1/index.html",{"error1":error1})
def sign_in(request):
    error_1=''
    error_2=''
    error_3=''
    usr = request.POST.get('username')
    pwd = request.POST.get('password')
    ged = request.POST.get('gender')
    age = request.POST.get('age')
    qq = int(time.time())
    if request.method == 'POST':
        #username的长度小于15，password大于6位，
        if len(request.POST.get('username')) <15:
            if len(request.POST.get('password'))>=6:
                if request.POST.get('gender')=='男' or request.POST.get("gender")=="女":
                    Userinfo.objects.create(qqid = qq ,password =pwd,username = usr,gender=ged,age = age)#QQ号由用户注册的时间决定
                    return render(request,'app1/sign_in_success.html',{"qqid":qq})
                else:
                    error_3="性别只能是男或女"
            else:
                error_2="密码不能小于6位"
        else:
            error_1 = "用户名不能超过15"

    return render(request,"app1/sign_in.html",{'error1':error_1,'error2':error_2,'error3':error_3})
def room(request,room_name):#房间号怎么确定？
    return render(request,"app1/home.html")
def person(request,qqid):
    data_list = Userinfo.objects.filter(qqid=qqid).all()
    for data in data_list:
        usr = data.username
    # print(qqid)问题：如何传入QQ给person界面，然后才能进行用户的个人操作

    return render(request,'app1/vi.html',{'qqid':qqid,'username':usr})
def user(request,qqid):
    data_list = Userinfo.objects.filter(qqid=qqid).all()
    for data in data_list:
        usr = data.username
        pwd = data.password
        ged = data.gender
        age = data.age
    return render(request,'app1/user.html',{'qqid':qqid,'username':usr,'gender':ged,'age':age})
def friends(request,qqid):
    data_list = Friend_relation.objects.filter(qqid=qqid)
    friends_list = []
    for friend in data_list:
        friends_list.append(friend.qqid_friend)
    data = Userinfo.objects.all()
    return render(request,'app1/friends.html',{'data':data,'friends_list':friends_list,'send_id':qqid})
def makefriends(request,qqid):
    #向数据库中的朋友表中插入两条数据
    add_qq=str(request.POST.get('qqid'))#添加的qq
    qqid=str(qqid)
    print(qqid,add_qq)
    users_list = Userinfo.objects.all()#获取所有用户qq号，包证添加用户存在
    friends_list = Friend_relation.objects.filter(qqid=qqid)
    qqid_list = []
    friendsqqid_list=[]
    for user in users_list:
        qqid_list.append(user.qqid)#获得所有的用户qq数组
    for friend in friends_list:
        friendsqqid_list.append(friend.qqid_friend)#获得所有的好友qq数组
    print(qqid_list,friendsqqid_list)
    #判断添加的好友qq是否存在
    if(add_qq not in qqid_list):
        result = {
            "success": False,
            "msg":"qq号不存在"
        }
    elif(add_qq in friendsqqid_list):
        result = {
            "success": False,
            "msg": "好友已存在"
        }
    elif add_qq==qqid:
        result = {
            "success": False,
            "msg": "不能添加自己"
        }
    else:
        result = {
            "success": True,
            "msg":"成功添加好友"
        }
        Friend_relation.objects.create(qqid=str(qqid), qqid_friend=str(add_qq))
        Friend_relation.objects.create(qqid=str(add_qq), qqid_friend=str(qqid))
    print(result['msg'])
    return JsonResponse(result)
    # return render(request, 'app1/VI.html')  # 朋友已存在，前端弹一个窗
def deletefriends(request,qqid):
    delete_qqid = str(request.POST.get('qqid'))  # 添加的qq
    qqid = str(qqid)
    print(qqid, delete_qqid)
    users_list = Userinfo.objects.all()  # 获取所有用户qq号，包证添加用户存在
    friends_list = Friend_relation.objects.filter(qqid=qqid)
    qqid_list = []
    friendsqqid_list = []
    for user in users_list:
        qqid_list.append(user.qqid)  # 获得所有的用户qq数组
    for friend in friends_list:
        friendsqqid_list.append(friend.qqid_friend)  # 获得所有的好友qq数组
    if (delete_qqid not in qqid_list):
        result = {
            "success": False,
            "msg": "qq号不存在"
        }
    elif (delete_qqid not in friendsqqid_list):
        result = {
            "success": False,
            "msg": "好友不存在"
        }
    else:
        result = {
            "success": True,
            "msg": "成功删除好友,请刷新"
        }
        #向数据库中删除一条数据
        Friend_relation.objects.filter(qqid=qqid, qqid_friend=delete_qqid).delete()
        Friend_relation.objects.filter(qqid=delete_qqid, qqid_friend=qqid).delete()
    return JsonResponse(result)
# def index1(request):
#     if request.method=='POST':
#         post_type = request.POST.get('post_type')
#         print(post_type)
#         if post_type == 'send_chat':
#             new_chat = Chat.objects.create(
#                 content=request.POST.get('content'),
#                 sender_id=request.session.get('qqid')
#             )
#             new_chat.save()
#             chats = Chat.objects.all()
#             return render(request, 'app1/chatroom.html', {'chats': chats})
#         elif post_type == 'get_chat':
#             chats = list(Chat.objects.all())[-100:]
#             print(chats[-1].content)
#             return render(request, 'app1/chatroom.html', {'chats': chats})
#         else:return HttpResponse("成功post")
#     else:
#         chats = list(Chat.objects.all())[-100:]
#         return render(request, 'app1/chatroom.html', {'chats': chats})
def index2(request,room_id):
    if request.method=='POST':
        post_type = request.POST.get('post_type')
        print(post_type)
        if post_type == 'send_chat':
            new_chat = Chat.objects.create(
                content=request.POST.get('content'),
                sender_id=request.session.get('qqid'),
                room_id=room_id
            )
            new_chat.save()
            chats = Chat.objects.filter(room_id=room_id)
            return render(request, 'app1/chatroom.html', {'chats': chats})
        elif post_type == 'get_chat':
            chats = Chat.objects.filter(room_id=room_id)
            return render(request, 'app1/chatroom.html', {'chats': chats})
        else:return HttpResponse("成功post")
    else:
        chats = Chat.objects.filter(room_id=room_id)
        return render(request, 'app1/chatroom.html', {'chats': chats})

