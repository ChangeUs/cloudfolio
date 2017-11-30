
from account.models import Account
from core.storage import PublicMediaStorage, PrivateMediaStorage
from core.models import *
from django.contrib.postgres.fields import ArrayField, JSONField

################################################################################


class Portfolio(TimeStampedModel):

    # Model constants #

    MAX_TITLE_LENGTH = 100

    PORTFOLIO_TYPE = (
        (1, "Personal"),
        (2, "Team"),
    )

    PORTFOLIO_TYPE_PERSONAL = 1
    PORTFOLIO_TYPE_TEAM = 2

    # Attributes of Portfolio model #

    account = models.ForeignKey(
        Account,
        related_name="portfolios",
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    portfolio_type = models.IntegerField(choices=PORTFOLIO_TYPE, default=1)

    # Meta information #

    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"
        ordering = ('account', 'created_time',)

    # Methods #

    def __str__(self):
        return self.title

    @staticmethod
    def make_portfolio(account, title=None):
        if title:
            portfolio = Portfolio(account=account, title=title)
        else:
            # the default title is "[Name] Portfolio"
            portfolio = Portfolio(account=account, title=account.__str__() + " Portfolio")

        portfolio.save()

        """Create a profile for this portfolio"""
        profile = Profile(portfolio=portfolio)
        profile.save()

        return portfolio

    def make_tab(self, title):
        tab = Tab(
            portfolio=self,
            title=title
        )

        tab.save()
        return tab

        tab.save()
        return tab

    def get_all_tabs(self, **kwargs):
        """
        If privacy does not exist in the parameter, return all tabs
        """
        if 'privacy' not in kwargs.keys():
            return self.tabs.all()

        return self.tabs.filter(privacy=kwargs['privacy'])


################################################################################


class Tab(TimeStampedModel):

    # Model constants #

    MAX_TITLE_LENGTH = 100

    # Attributes of Tab model #

    portfolio = models.ForeignKey(
        Portfolio,
        related_name="tabs",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH)

    # Meta information #

    class Meta:
        verbose_name = "tab"
        verbose_name_plural = "tabs"
        ordering = ('portfolio', 'created_time',)

    # Methods #

    def __str__(self):
        return self.title

    def make_activity(self, title, summary):
        activity = Activity(
            tab=self,
            portfolio=self.portfolio,
            title=title,
            summary=summary)

        activity.save()
        return activity

    def make_activity(self, title, summary, privacy):
        activity = Activity(
            tab=self,
            portfolio=self.portfolio,
            title=title,
            summary=summary,
            privacy=privacy)

        activity.save()
        return activity

    def get_all_activities(self, **kwargs):
        """
        If privacy does not exist in the parameter, return all activities
        """
        if 'privacy' not in kwargs.keys():
            return self.activities.all()

        return self.activities.filter(privacy=kwargs['privacy'])

    def get_public_activities(self):
        return self.get_all_activities(privacy=PrivacyModel.PUBLIC_ALL)


################################################################################


class Activity(TimeStampedModel, FormatOfPeriodModel, PrivacyModel):

    # Model constants #

    MAX_TITLE_LENGTH = 100
    MAX_SUMMARY_LENGTH = 100

    # Attributes of Activity model #

    portfolio = models.ForeignKey(
        Portfolio,
        related_name="activities",
    )
    tab = models.ForeignKey(
        Tab,
        related_name="activities",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    summary = models.CharField(max_length=MAX_SUMMARY_LENGTH)

    # Meta information #

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"
        ordering = ('tab', 'created_time', )

    # Methods #

    def __str__(self):
        return self.title

    def make_story(self, title, content):
        story = Story(
            activity=self,
            portfolio=self.portfolio,
            title=title,
            content=content)

        story.save()
        return story

    def make_story(self, title, content, privacy):
        story = Story(
            activity=self,
            portfolio=self.portfolio,
            title=title,
            content=content,
            privacy=privacy)

        story.save()
        return story

    def get_all_stories(self, **kwargs):
        """
        If privacy does not exist in the parameter, return all stories
        """
        if 'privacy' not in kwargs.keys():
            return self.stories.all()

        return self.stories.filter(privacy=kwargs['privacy'])

    def get_public_stories(self):
        return self.get_all_stories(privacy=PrivacyModel.PUBLIC_ALL)


################################################################################

class Story(TimeStampedModel, FormatOfPeriodModel, PrivacyModel):

    # Model constants #

    MAX_TITLE_LENGTH = 100
    MAX_PATH_LENGTH = 255

    # Attributes of Story model #

    portfolio = models.ForeignKey(
        Portfolio,
        related_name="stories"
    )
    activity = models.ForeignKey(
        Activity,
        related_name="stories",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH, blank=True, default="")
    content = models.TextField()

    image_files = ArrayField(models.FileField(), blank=True, null=True)
    uploaded_files = ArrayField(models.FileField(), blank=True, null=True)

    # Meta information #

    class Meta:
        verbose_name = "story"
        verbose_name_plural = "stories"
        ordering = ('activity', 'created_time',)

    # Methods #

    def __str__(self):
        return self.title


################################################################################


class Profile(TimeStampedModel):

    # Attributes of Profile model #

    portfolio = models.OneToOneField(Portfolio, auto_created=True)
    profile = JSONField(default={})

    # Meta information #

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        ordering = ('portfolio', )

    # Methods #

    def get_profile(self, title=None):
        if title is None:
            return self.profile
        return self.profile[title]

    def get_public_profile(self):
        profile = {}

        for field, info in self.profile.items():
            if isinstance(info, list):
                arr = []
                for profile_info in info:
                    if profile_info.get('public'):
                        arr.append(profile_info)

                if len(arr) > 0:
                    profile.update({field: arr})

            else:
                if info.get('public'):
                    profile.update({field: info})

        return profile

################################################################################


def story_file_path(instance, filename):
    return '/'.join(['story', '{0}', '{1}']).format(instance.story_id, filename)


class FileContent(models.Model):

    # Attributes of FileContent model #

    uploaded_at = models.DateTimeField(auto_now_add=True)

    story = models.ForeignKey(
        Story,
        related_name="files"
    )

    file = models.FileField(upload_to=story_file_path, storage=PrivateMediaStorage())

    class Meta:
        verbose_name = "file"
        verbose_name_plural = "files"
        ordering = ('story', )


class Resume(TimeStampedModel):

    # Attributes of Profile model #

    portfolio = models.OneToOneField(Portfolio, auto_created=True)
    contents = JSONField(default={})

    class Meta:
        verbose_name = "resume"
        verbose_name_plural = "resumes"
        ordering = ('portfolio', )