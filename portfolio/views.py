from django.shortcuts import render
from django.views.generic import View
from portfolio.models import Portfolio
from portfolio.forms import *
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from portfolio.profile import ProfileInfo

# Create your views here.

from django.template.defaultfilters import register

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


class ActivityCreateView(View):

    def get(self, request, tab_id):
        if not check_user_login(request):
            return HttpResponse(status=400)

        form = ActivityCreationForm()

        context = {
            'form': form,
            'tab_id': tab_id
        }

        return render(request, 'portfolio/activity-create.html', context)


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

        context = {
            'profile': profile
        }

        return render(request, 'portfolio/profile_info.html', context)


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

        return render(request, 'portfolio/profile_info.html', context)


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
