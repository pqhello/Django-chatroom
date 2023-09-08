from django.urls import path

from . import views

urlpatterns = [
    # path('index1', views.index1,name='index1'),#聊天框
    path('<str:room_id>/index2', views.index2,name='index1'),#聊天框
    path('index', views.index,name='index'),
    path('sign_in', views.sign_in,name='hello'),#==>这里匹配的路径是/polls/hello
    path('room/<str:room_name>/', views.room, name='room'),
    path('person/<str:qqid>/',views.person,name='person'),
    path('person/<int:qqid>/user',views.user,name='user'),
    path('person/<int:qqid>/friends',views.friends,name='friends'),
    path('person/<int:qqid>/makefriends',views.makefriends,name='makefriends'),
    path('person/<int:qqid>/deletefriends', views.deletefriends, name='deletefriends'),

]