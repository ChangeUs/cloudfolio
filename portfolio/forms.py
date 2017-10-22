
from __future__ import unicode_literals
from django import forms

from portfolio.models import *

################################################################################


class TabCreationForm(forms.ModelForm):

    class Meta:
        model = Tab
        fields = ('title',)


################################################################################


class ActivityCreationForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('title', 'summary', 'start_time', 'end_time')


################################################################################


class StoryCreationForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'start_time', 'end_time', 'content', 'image_files', 'uploaded_files')


################################################################################


class ProfileForm(forms.Form):

    MULTIPLE = False

    public = forms.BooleanField(
        required=False,
        label="공개",
        widget=forms.CheckboxInput
    )

    def save(self):
        return self.cleaned_data


class OccupationForm(ProfileForm):

    occupation = forms.CharField(
        required=False,
        label="직군",
        strip=False,
        widget=forms.TextInput
    )


class IntroductionForm(ProfileForm):

    introduction = forms.CharField(
        required=False,
        label="한줄 프로필",
        strip=False,
        widget=forms.TextInput
    )


class BirthdayForm(ProfileForm):

    birthday = forms.DateField(
        required=False,
        label="생일",
        widget=forms.DateInput
    )


class EducationForm(ProfileForm):

    MULTIPLE = True

    school = forms.CharField(
        required=False,
        label='학교',
        widget=forms.TextInput
    )

    degree = forms.CharField(
        required=False,
        label="학위",
        widget=forms.TextInput
    )

    major = forms.CharField(
        required=False,
        label="전공",
        widget=forms.TextInput
    )

    start_date = forms.DateField(
        required=False,
        label="시작일",
        widget=forms.DateInput
    )

    end_date = forms.DateField(
        required=False,
        label="종료일",
        widget=forms.DateInput
    )

    in_school = forms.BooleanField(
        required=False,
        label="재학 중",
        widget=forms.CheckboxInput
    )

