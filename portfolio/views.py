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


################################################################################


@register.filter(name="isinstance")
def isinstance_filter(val, instance_type):
    return isinstance(val, eval(instance_type))


def check_user_login(request):
    """
    Check whether the current user is logged in or not.
    :param request: request parameter of view.
    :return: True if logged in or False if anonymous user.
    """
    if request.user.is_anonymous():
        return False
    return True

################################################################################

# TODO: class기반의 view로 바꿔주면 백단에서 더욱편함.
# 현재는 프론트단을 위해 임시로 def를 만든 것.
def portfolioIndexView(request):
    return render(request, 'portfolio/index.html')
def portfolioBaseView(request):
    return render(request, 'portfolio/base.html')


def portfolio_main_view(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    return render(request, 'portfolio/index.html', {'user': request.user, 'portfolio': portfolio})


################################################################################

class ActivityView(View):

    def get(self, request, pk):
        if not check_user_login(request):
            return HttpResponse(status=400)

        try:
            portfolio = request.user.get_user_portfolio()
            tab = portfolio.tabs.get(pk=pk)
            act = portfolio.activities.get(pk=pk)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        portfolio = request.user.get_user_portfolio()
        profile = portfolio.profile.get_profile()

        activityCreateForm = ActivityCreationForm()
        tabCreationForm = TabCreationForm()


        context = {
            'portfolio': portfolio,
            'tab': tab,
            'profile': profile,
            'activityCreateForm': activityCreateForm,
            'tabCreationForm': tabCreationForm,
            'activity' : act
        }

        return render(request, 'portfolio/activity.html', context)


class ActivityCreateView(View):

    def get(self, request, tab_id):
        if not check_user_login(request):
            return HttpResponse(status=400)

        portfolio = request.user.get_user_portfolio()
        profile = portfolio.profile.get_profile()
        tab = portfolio.tabs.get(pk=tab_id)
        activityCreateForm = ActivityCreationForm()
        tabCreationForm = TabCreationForm()

        context = {
            'portfolio': portfolio,
            'tab' : tab,
            'profile': profile,
            'activityCreateForm': activityCreateForm,
            'tabCreationForm': tabCreationForm,
        }

        return render(request, 'portfolio/activity_create.html', context)

    def post(self, request, tab_id):
        if not check_user_login(request):
            return HttpResponse(status=400)
        try:
            portfolio = request.user.get_user_portfolio()
            activity_tab = portfolio.tabs.get(pk=tab_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)
        form = ActivityCreationForm(request.POST)
        if form.is_valid():
            act = form.save(commit=False)
            act.portfolio = portfolio
            act.tab = activity_tab
            act.save()

            messages.success(request, _('액티비티를 등록했습니다.'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            return HttpResponse(status=400)


class ActivityDeleteView(View):

    def get(self, request, activity_id):
        if not check_user_login(request):
            return HttpResponse(status=400)

        try:
            portfolio = request.user.get_user_portfolio()
            act = portfolio.activities.get(pk=activity_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        act.delete()
        return HttpResponse(status=200)


################################################################################


class StoryCreateView(View):

    def get(self, request, activity_id):
        if not check_user_login(request):
            return HttpResponse(status=400)

        portfolio = request.user.get_user_portfolio()
        profile = portfolio.profile.get_profile()

        activityCreateForm = ActivityCreationForm()
        tabCreationForm = TabCreationForm()
        storyCreationForm = StoryCreationForm()

        context = {
            'portfolio': portfolio,
            'tab': tab,
            'profile': profile,
            'activityCreateForm': activityCreateForm,
            'tabCreationForm': tabCreationForm,
            'storyCreationForm': storyCreationForm,
        }

        return render(request, 'portfolio/story-create.html', context)

    def post(self, request, activity_id):
        if not check_user_login(request):
            return HttpResponse(status=400)

        try:
            portfolio = request.user.get_user_portfolio()
            act = portfolio.activities.get(pk=activity_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        form = StoryCreationForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.portfolio = portfolio
            story.activity = act
            story.save()

            return HttpResponse(status=200)

        else:
            return HttpResponse(status=400)


class StoryDeleteView(View):

    def get(self, request, story_id):
        if not check_user_login(request):
            return HttpResponse(status=400)

        try:
            portfolio = request.user.get_user_portfolio()
            story = portfolio.stories.get(pk=story_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        story.delete()
        return HttpResponse(status=200)


################################################################################


class TabCreateView(View):

    def get(self, request):
        if not check_user_login(request):
            return HttpResponse(status=400)

        form = TabCreationForm()

        context = {
            'form': form,
        }
        return render(request, 'portfolio/tab-create.html', context)

    def post(self, request):
        if not check_user_login(request):
            return HttpResponse(status=400)

        try:
            portfolio = request.user.get_user_portfolio()
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        form = TabCreationForm(request.POST)

        if form.is_valid():
            tab = form.save(commit=False)
            tab.portfolio = portfolio
            tab.save()

            # return HttpResponse(status=200)

            # 포스트 완료 메세지
            messages.success(request, _('탭을 등록했습니다.'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse(status=400)



class TabDeleteView(View):

    def get(self, request, tab_id):
        if not check_user_login(request):
            return HttpResponse(status=400)

        try:
            portfolio = request.user.get_user_portfolio()
            tab = portfolio.tabs.get(pk=tab_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        tab.delete()
        return HttpResponse(status=200)


class TabView(View):

    def get(self, request, pk):
        if not check_user_login(request):
            return HttpResponse(status=400)

        try:
            portfolio = request.user.get_user_portfolio()
            tab = portfolio.tabs.get(pk=pk)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        portfolio = request.user.get_user_portfolio()
        profile = portfolio.profile.get_profile()

        activityCreateForm = ActivityCreationForm()
        tabCreationForm = TabCreationForm()


        context = {
            'portfolio': portfolio,
            'tab': tab,
            'profile': profile,
            'activityCreateForm': activityCreateForm,
            'tabCreationForm': tabCreationForm,
        }

        return render(request, 'portfolio/tab.html', context)


################################################################################


class ProfileView(View):

    """
    Render current user portfolio profile.
    This view shows all information including private profile.
    """
    def get(self, request):
        if not check_user_login(request):
            return HttpResponse(status=400)

        """Get portfolio and profile from user"""
        portfolio = request.user.get_user_portfolio()
        profile = portfolio.profile.get_profile()

        tabCreationForm = TabCreationForm()
        context = {
            'tabCreationForm' : TabCreationForm,
            'portfolio': portfolio,
            'profile': profile
        }

        return render(request, 'portfolio/profile.html', context)


################################################################################


class ProfilePublicView(View):

    def get(self, request, pk):

        """
        Render an user profile only public checked.
        :param pk: primay key or the portfolio.
        """

        try:
            """Get portfolio and profile from user primary key"""
            portfolio = Portfolio.objects.get(pk=pk)
            profile = portfolio.profile.get_public_profile()

        except ObjectDoesNotExist:
            """If the portfolio does not exist, return with error code"""
            return HttpResponse(status=404)

        context = {
            'profile': profile
        }

        return render(request, 'portfolio/profile.html', context)


################################################################################


class ProfileEditView(View):

    def get(self, request):

        """
        Renders editing view for current user portfolio profile.
         It needs "profile" parameter by GET method. "profile" parameter represents
        the profile information to edit and the domain of "profile" parameter is
        defined in profile.py.
        :return: rendered html for editing portfolio profile.
        """

        if not self.check_all(request):
            return HttpResponse(status=400)

        """Get portfolio and profile from user"""
        profile_form = ProfileInfo.get_profile_form(request.GET['profile'])

        form = profile_form()
        context = {'profile_form': form}
        return render(request, 'portfolio/profile-edit.html', context)

    def post(self, request):

        """
        Edits portfolio profile for an user.
         It needs "profile" parameter by GET method and it needs "index" parameter
        more if the profile is array. "profile" parameter represents the profile
        information to edit and "index" represents the array index to change when
        the profile is array.
        :return: status 200 code if successfully edited, or status 400 if not.
        """

        if not self.check_all(request):
            return HttpResponse(status=400)

        """Get portfolio and profile from user"""
        portfolio = request.user.get_user_portfolio()
        profile = portfolio.profile
        profile_title = request.GET['profile']
        profile_form = ProfileInfo.get_profile_form(request.GET['profile'])

        form = profile_form(request.POST)

        if form.is_valid():

            """If the profile is multiple information"""
            if profile_form.MULTIPLE:

                """
                It needs index for editing.
                If index is not exist, it adds a new data to the array
                """
                if 'index' not in request.GET:
                    json_data = profile.profile
                    json_field_data = json_data.get(profile_title)

                    if json_field_data is None:
                        json_data.update({profile_title: []})
                        json_field_data = json_data.get(profile_title)

                    json_field_data.append(form.save())
                    profile.save()
                    return HttpResponse(status=200)

                try:
                    profile_index = int(request.GET['index'])
                except ValueError:
                    return HttpResponse(status=400)

                json_data = profile.profile

                if profile_title in json_data:
                    json_field_data = json_data.get(profile_title)

                    try:
                        json_field_data[profile_index] = form.save()
                    except IndexError:
                        return HttpResponse(status=400)

                else:
                    json_data.update({profile_title: [form.save(), ]})

                profile.save()

                """Return success"""
                return HttpResponse(status=200)

            else:
                """Get JSON data from profile and update"""
                json_data = profile.profile
                json_data.update({profile_title: form.save()})

                profile.profile = json_data
                profile.save()

                """Return success"""
                return HttpResponse(status=200)

        return HttpResponse(status=400)

    @staticmethod
    def check_parameter(request):
        """
        Checks "profile" parameter by GET method exists or not.
        :return: True if exist or false if not exist.
        """
        if 'profile' not in request.GET:
            return False
        return True

    @staticmethod
    def check_parameter_value(request):
        """
        Checks whether "profile" parameter is in domain.
        :return: True if in or false if not in.
        """
        profile_value = request.GET['profile']
        """if "profile" parameter value is not registered profile info"""
        if profile_value not in ProfileInfo.PROFILE:
            return False
        return True

    def check_all(self, request):
        """
        Checks "profile" parameter is appropriate and signed in.
        :return: True if all condition satisfies or false if not.
        """
        if self.check_parameter(request) and self.check_parameter_value(request) and check_user_login(request):
            return True
        return False


################################################################################

class GalleryView(View):

    def get(self, request, portfolio_id):

        try:
            portfolio = Portfolio.objects.get(pk=portfolio_id)
            profile = portfolio.profile.get_public_profile()
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        context = {'portfolio':portfolio, 'profile':profile}

        return render(request, 'portfolio/gallery.html', context)


################################################################################

class ResumeView(View):

    def get(self, request):

        try:
            portfolio = request.user.get_user_portfolio()
            profile = portfolio.profile.get_public_profile()
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        context = {'portfolio':portfolio, 'profile':profile}

        return render(request, 'portfolio/resume-default.html', context)


# 임시


def activity(request):
    return render(request, 'portfolio/activity.html')


def activity_edit(request):
    return render(request, 'portfolio/activity_edit.html')


def tab(request):
    return render(request, 'portfolio/tab.html')

def story_edit(request):
    context = { 'portfolio':request.user.get_user_portfolio() }
    return render(request, 'portfolio/story_edit.html', context)

def profile_temp(request):
    return render(request, 'portfolio/profile.html')
