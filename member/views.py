from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.context_processors import messages
# Create your views here.
from django.template.context_processors import request
from django.views.generic import DetailView, CreateView

import member
from member.models import Member


# 시작 페이지로 이동
def Main(request):
    return render(request, 'member/main.html')


def Create_member(request):
    return render(request, 'member/sign_up.html')


def Sign_in(request):
    return render(request, 'member/sign_in.html')


def Sign_up(request):
    # POST객체로 받아온것들 변수에 저장

    uesr_id = request.POST['user_id']
    pw = request.POST['password']
    name = request.POST['name']
    current_residence = request.POST['current_residence']
    preferred_residence = request.POST['preferred_residence']

    check_id = ''
    try:
        check = Member.objects.get(user_id=uesr_id)
        check_id = check.user_id
    except ObjectDoesNotExist:
        check_id = ''
    # 아이디가 같을경우 안됨
    yes_or_no = ''
    print('받아온 id : ' + uesr_id)
    print('확인할 id : ' + check_id)

    if uesr_id == check_id:
        yes_or_no = '아이디가 중복되었습니다. 수정이 필요합니다.'
        print('아이디 중복')
    # 성공했을 경우 메세지 출력 (디비에 데이터 넣음)
    else:
        data = Member(user_id=uesr_id, pw=pw, name=name, current_residence=current_residence,
                      preferred_residence=preferred_residence)
        data.save()
        print('디비 들어감')
        yes_or_no = '회원가입 완료!'

    print(yes_or_no)
    return render(request, 'member/check.html', {'data': yes_or_no})


def Signin(request):
    id = request.POST['user_id']
    pw = request.POST['pw']
    print("id : " + id + " pw : " + pw)
    check = ''
    try:
        query_set = Member.objects.get(user_id=id, pw=pw)
    except ObjectDoesNotExist:
        check = 'N'
    print(check)
    message = ''
    if check == 'N':
        message = '아이디 혹은 비밀번호를 확인해주세요.'
    else:
        message = '로그인 성공!'
    return render(request,'member/check.html',{'data' : message})

# def Member_create(request):
#     print("def_Member_create에 잘옴")
#     return render(request,'member/member_create.html')
#
#
# def  Test(request):
#     return render(request,'member/login.html')
#
# def Member_id_check(request):
#     try:
#         id = Member.objects.get(user_id=request.GET['id'])
#     except Exception as e:
#         id = None
#     result = {
#         'result' : 'success',
#         'data' : "not exist" if id is None else "exist"
#     }
#     return JsonResponse(result)
#
# def Member_insert(request):
#     print('Member_insert에 도착함.')
#     print("method 인식")
#     if request.method == 'POST':
#         print("method 인식")
#         form = request.POST
#         id = form.user_id
#         pw = form.pw
#         name = form.name
#         current_residence = form.current_residence
#         preferred_residence = form.preferred_residence
#         print(id , pw , name , preferred_residence , current_residence)
#         if form.is_valid():
#             form.save()
#             print('POST인식함! 디비 들어감!')
#         return redirect('/member/login.html')
#     else:
#         form = MemberForm()
#     print('POST인식 못함 , 디비 안들어감')
#     return render(request,'member/login.html')
