from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from account.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# 회원가입
def signup(request):

    # 기로그인 -> redirect
    if request.user.is_anonymous:
        pass
    elif request.user:
        return HttpResponseRedirect('/portfolios/')

    template = 'registration/signup.html'
    signupForm = UserCreationForm()
    message = ""

    # form 작성 후 post 액션 시
    if request.method == "POST":
        signupForm = UserCreationForm(request.POST, request.FILES or None)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()
            # TODO: 이메일 인증 기능 추가 필요
            return HttpResponse('회원가입 완료')
        else:
            message="패스워드 미일치"

    elif request.method == "GET":
        pass

    context = {"signupForm": signupForm, "message": message}
    return render(request, template, context)


#로그인
def signin(request):
    template = 'registration/login.html'
    message = ""

    # form 작성 후 post 액션 시
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('로그인 성공 ' + email + " " + password)
            else:
                return HttpResponse("Your account is not active, please contact the site admin")
        else:
            return HttpResponse("로그인 실패 : Your username and/or password were incorrect")
    else:
        context = {"message": message}
        return render(request, template, context)


#로그아웃
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')


