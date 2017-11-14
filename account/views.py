from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site

from account.models import Account
from portfolium import settings
from .tokens import account_activation_token

from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from portfolio.models import Portfolio
# from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from account.forms import UserCreationForm, PasswordChangeFormCustom


# 회원가입
def signup(request):

    # 기로그인 -> redirect
    if request.user.is_anonymous:
        pass
    elif request.user:
        # return HttpResponseRedirect('/portfolios/')
        return HttpResponseRedirect('/')

    template = 'registration/signup.html'
    signupForm = UserCreationForm()
    message = ""

    # form 작성 후 post 액션 시
    if request.method == "POST":
        signupForm = UserCreationForm(request.POST, request.FILES or None)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()

            """Create a portfolio for this user"""
            Portfolio.make_portfolio(user)

            # 계정 활성화를 위한 이메일 인증
            current_site = get_current_site(request)

            mail_subject = render_to_string('registration/activation_email_subject.txt')
            mail_message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
            })
            to_email = signupForm.cleaned_data.get('email')

            email = EmailMessage(
                mail_subject, mail_message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            message="패스워드 미일치"

    elif request.method == "GET":
        pass

    context = {"signupForm": signupForm, "message": message}
    return render(request, template, context)


#회원탈퇴
def delete_user(request):
    user = Account.objects.get(email=request.user.email)
    user.delete()
    # user.is_active = False
    # user.save(update_fields=['is_active'])

    return redirect('/')


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
                messages.success(request, _('로그인에 성공했습니다'))
                # TODO: 로그인 성공시 프로필화면
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("Your account is not active, please contact the site admin")
        else:
            # TODO: 로그인 실패 메세지 구현
            return HttpResponse("로그인 실패 : Your username and/or password were incorrect")
    else:
        # get
        # TODO: 로그인 계정의 is_active에따라 redirect 다르게 설정 필요
        if request.user.is_anonymous:
            context = {"message": message}
            return render(request, template, context)
        else:
            redirect_url = reverse('portfolios:profile')
            return redirect(redirect_url)





#로그아웃
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')


#계정 활성화 승인
def activate(request, uidb64, token):
    template1 = 'registration/activation_complete.html'
    template2 = 'registration/activation.html'

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, template1)
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return render(request, template2)
        # return HttpResponse('Activation link is invalid!')

#회원탈퇴
def delete_user(request):
    user = Account.objects.get(email=request.user.email)
    user.delete()
    # user.is_active = False
    # user.save(update_fields=['is_active'])

    return HttpResponseRedirect('/')

#비밀번호 변경
@login_required
def change_password(request):
    template1 = 'registration/password_change_form.html'
    template2 = 'registration/password_change_done.html'

    if request.method == 'POST':
        form = PasswordChangeFormCustom(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, template2)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeFormCustom(request.user)

    return render(request, template1, {
        'form': form
    })



