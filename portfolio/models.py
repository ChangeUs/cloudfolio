
from account.models import Account
from core.models import *
from django.contrib.postgres.fields import ArrayField

################################################################################


class Portfolio(TimeStampedModel):

    # Model constants #

    MAX_TITLE_LENGTH = 100

    # Attributes of Portfolio model #

    account = models.ForeignKey(
        Account,
        related_name="portfolios",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH)

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
            portfolio = Account(title=title)
        else:
            # the default title is "[Name] Portfolio"
            portfolio = Account(title=account.__str__() + " Portfolio")

        portfolio.save()
        return portfolio

    def make_tab(self, title):
        tab = Tab(
            portfolio=self.id,
            title=title
        )

        tab.save()
        return tab

    def make_tab(self, title, privacy):
        tab = Tab(
            portfolio=self.id,
            title=title,
            privacy=privacy
        )

        tab.save()
        return tab

    def get_all_tabs(self, **kwargs):
        """
        If privacy does not exist in the parameter, return all tabs
        """
        if 'privacy' in kwargs:
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
            tab=self.id,
            title=title,
            summary=summary)

        activity.save()
        return activity

    def make_activity(self, title, summary, privacy):
        activity = Activity(
            tab=self.id,
            title=title,
            summary=summary,
            privacy=privacy)

        activity.save()
        return activity

    def get_all_activities(self, **kwargs):
        """
        If privacy does not exist in the parameter, return all activities
        """
        if 'privacy' in kwargs:
            return self.activities.all()

        return self.activities.filter(privacy=kwargs['privacy'])


################################################################################


class Activity(TimeStampedModel, FormatOfPeriodModel, PrivacyModel):

    # Model constants #

    MAX_TITLE_LENGTH = 100
    MAX_SUMMARY_LENGTH = 100

    # Attributes of Activity model #

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
            activity=self.id,
            title=title,
            content=content)

        story.save()
        return story

    def make_story(self, title, content, privacy):
        story = Story(
            activity=self.id,
            title=title,
            content=content,
            privacy=privacy)

        story.save()
        return story

    def get_all_stories(self, **kwargs):
        """
        If privacy does not exist in the parameter, return all stories
        """
        if 'privacy' in kwargs:
            return self.stories.all()

        return self.stories.filter(privacy=kwargs['privacy'])


################################################################################

class Story(TimeStampedModel, FormatOfPeriodModel, PrivacyModel):

    # Model constants #

    MAX_TITLE_LENGTH = 100
    MAX_PATH_LENGTH = 255

    # Attributes of Story model #

    activity = models.ForeignKey(
        Activity,
        related_name="stories",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH, blank=True, default="")
    content = models.TextField()

    image_files = ArrayField(models.CharField(max_length=MAX_PATH_LENGTH), blank=True)
    uploaded_files = ArrayField(models.CharField(max_length=MAX_PATH_LENGTH), blank=True)

    # Meta information #

    class Meta:
        verbose_name = "story"
        verbose_name_plural = "stories"
        ordering = ('activity', 'created_time',)

    # Methods #

    def __str__(self):
        return self.title


################################################################################
