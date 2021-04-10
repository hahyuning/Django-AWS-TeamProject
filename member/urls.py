from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view

import member.views

urlpatterns = [
    # path('login/', member.views.Test, name='login'),
    # path('signin/',member.views.Member_create , name='signin'),
    # path('member/signin/idcheck/',member.views.Member_id_check , name='idcheck'),
    # path('member/signin/insert/', member.views.Member_insert,name='member_insert'),
    # path('login/', auth_view.LoginView.as_view(), name='new_login'),
    path('signup/',member.views.Create_member,name='create_member'),
    path('signin/',member.views.Sign_in,name='sign_in'),
    path('signup/check',member.views.Sign_up,name='sign_up'),
    path('signin/check',member.views.Signin,name='signin')
]