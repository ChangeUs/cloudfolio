
from __future__ import unicode_literals
from django import forms

from portfolio.models import *

################################################################################


class TabCreationForm(forms.ModelForm):

    class Meta:
        model = Tab
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super(TabCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
          'class' : 'form-control',
        })


################################################################################


class ActivityCreationForm(forms.ModelForm):

    summary = forms.CharField(
     widget=forms.Textarea(attrs={
         'placeholder': '간략한 활동의 설명을 적어주세요 (100자 미만)',
         'rows' : 4,
         'maxlength' : 100,
     }))
    class Meta:
        model = Activity
        fields = ('title', 'summary', 'start_time', 'end_time')

    def __init__(self, *args, **kwargs):
        super(ActivityCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
          'class' : 'bold',
          'placeholder' : '제목을 입력하세요',
        })



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


class ContactForm(ProfileForm):

    mobile_phone_number = forms.CharField(
        required=False,
        label="휴대폰",
        strip=False,
        widget=forms.TextInput
    )

    phone_number = forms.CharField(
        required=False,
        label="전화번호",
        strip=False,
        widget=forms.TextInput
    )


class AddressForm(ProfileForm):

    residence = forms.CharField(
        required=False,
        label="거주지",
        strip=False,
        widget=forms.TextInput
    )

    active_area = forms.CharField(
        required=False,
        label="활동지역",
        strip=False,
        widget=forms.TextInput
    )


class InterestKeywordsForm(ProfileForm):

    MULTIPLE = True

    interest_keyword = forms.CharField(
        required=False,
        label="관심 키워드",
        strip=False,
        widget=forms.TextInput
    )


class HomepageForm(ProfileForm):

    facebook_page = forms.CharField(
        required=False,
        label="facebook",
        strip=False,
        widget=forms.TextInput
    )

    twitter_page = forms.CharField(
        required=False,
        label="twitter",
        strip=False,
        widget=forms.TextInput
    )

    instagram_page = forms.CharField(
        required=False,
        label="instagram",
        strip=False,
        widget=forms.TextInput
    )

    github_page = forms.CharField(
        required=False,
        label="github",
        strip=False,
        widget=forms.TextInput
    )

    linkedin_page = forms.CharField(
        required=False,
        label="linkedin",
        strip=False,
        widget=forms.TextInput
    )

    behance_page = forms.CharField(
        required=False,
        label="behance",
        strip=False,
        widget=forms.TextInput
    )

    blog_page = forms.URLField(
        required=False,
        label="blog(URL만)",
        widget=forms.URLInput
    )


class CertificateForm(ProfileForm):

    MULTIPLE = True

    title = forms.CharField(
        required=False,
        label='제목',
        widget=forms.TextInput
    )

    organizer = forms.CharField(
        required=False,
        label='주최',
        widget=forms.TextInput
    )

    acquisition_date = forms.DateField(
        required=False,
        label='취득일',
        widget=forms.DateInput
    )

    certificate_file = forms.FileField(
        required=False,
        label='증명서',
        widget=forms.FileInput
    )


class LanguageForm(ProfileForm):

    MULTIPLE = True

    CHOICES = (
        ('1', '미흡'),
        ('2', '보통'),
        ('3', '유창'),
    )

    language_name = forms.CharField(
        required=False,
        label='언어명',
        widget=forms.TextInput
    )

    level = forms.ChoiceField(
        required=False,
        label='수준',
        widget=forms.Select,
        choices=CHOICES
    )


# class PercentageInput(forms.TextInput):
#     def render(self, name, value, attrs=None):
#         try:
#             value = float(value)
#             value *= 100
#         except ValueError:
#             pass
#         return super(PercentageInput, self).render(name, value, attrs)
#
#
# class PercentageField(forms.FloatField):
#     widget = PercentageInput
#
#     def to_python(self, value):
#         value = super(PercentageField, self).to_python(value)
#         return value / 100


class TechnologyForm(ProfileForm):

    MULTIPLE = True

    technology_name = forms.CharField(
        required=False,
        label='기술명',
        widget=forms.TextInput
    )

    level = forms.IntegerField(
        required=False,
        label='수준',
        widget=forms.NumberInput
    )
