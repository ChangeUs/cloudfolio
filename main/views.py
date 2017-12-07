from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import register

from portfolio.models import Portfolio
from portfolio.forms import *
from portfolio.profile import ProfileInfo
from portfolio.views import check_user_login


class ShowboxView(View):

    def get(self, request):
        if not check_user_login(request):
            return HttpResponse(status=400)

        portfolio = request.user.get_user_portfolio()
        profile = portfolio.profile.get_profile()
        activityCreateForm = ActivityCreationForm()
        tabCreationForm = TabCreationForm()

        context = {
            'portfolio': portfolio,
            'profile': profile,
            'activityCreateForm': activityCreateForm,
            'tabCreationForm': tabCreationForm,
        }

        return render(request, 'portfolio/showbox.html', context)


# 샘플 이력서
def resume_sample_1(request):
    if not check_user_login(request):
        return HttpResponse(status=400)

    portfolio = request.user.get_user_portfolio()
    tab = portfolio.get_all_tabs()
    profile = portfolio.profile.get_profile()

    context = {
        'portfolio': portfolio,
        'tab' : tab,
        'profile': profile,
    }

    return render(request, 'resume_sample/sample1/index.html', context)

def resume_sample_2(request):
    if not check_user_login(request):
        return HttpResponse(status=400)

    portfolio = request.user.get_user_portfolio()
    profile = portfolio.profile.get_profile()
    tab = portfolio.get_all_tabs()

    context = {
        'portfolio': portfolio,
        'tab': tab,
        'profile': profile,
    }
    return render(request, 'resume_sample/sample2/education.html', context)
