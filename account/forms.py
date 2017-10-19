from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
# from django.contrib.auth import password_validation
from account.models import Account


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        # html 상에서 form 태그의 input들이 가질 name
        fields = ("name", "email", "password1", "password2")

    # 에러메세지 설정
    error_messages = {
        'password_mismatch': _("패스워드가 일치하지 않습니다."),
    }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


    # html에 tag로 생성됨
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
          'class' : 'form-control',
          'placeholder' : '이메일은 로그인 아이디로 사용됩니다',
        })
        self.fields['name'].widget.attrs.update({
          'class' : 'form-control',
          'placeholder' : '이름을 입력하세요',
        })
        self.fields['password1'].widget.attrs.update({
          'class' : 'form-control',
            'placeholder' : '패스워드를 입력하세요',
        })
        self.fields['password2'].widget.attrs.update({
          'class' : 'form-control',
            'placeholder' : '패스워드를 확인해주세요',
        })

    # form을 통해 받은 데이터를 저장
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("email", "name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)

    error_messages = {
        'password_mismatch': _("패스워드가 일치하지 않습니다."),
    }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def save(self, user):
        user.save()
