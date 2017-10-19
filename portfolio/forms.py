
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

