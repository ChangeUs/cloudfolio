
from django.db import models
from account.models import Account

################################################################################


class Portfolio(models.Model):

    # Attributes of Portfolio model #

    account = models.ForeignKey(Account, related_name="portfolios")

    # Meta information #

    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"

        # TODO: ordering by created_at
        """
            ordering = ('created_at')
        """

    # Methods #

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


################################################################################


class Tab(models.Model):

    # Model constants #

    MAX_TITLE_LENGTH = 100

    # Attributes of Tab model #

    portfolio = models.ForeignKey(Portfolio, related_name="tabs")

    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    privacy = models.IntegerField(default=0)

    # Meta information #

    class Meta:
        verbose_name = "tab"
        verbose_name_plural = "tabs"

        # TODO: ordering by created_at
        """
            ordering = ('created_at')
        """

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


################################################################################


class Activity(models.Model):

    # Model constants #

    MAX_TITLE_LENGTH = 100
    MAX_SUMMARY_LENGTH = 100

    # Attributes of Activity model #

    tab = models.ForeignKey(Tab, related_name="activities")

    title = models.CharField(max_length=MAX_TITLE_LENGTH, default="")
    summary = models.CharField(max_length=MAX_SUMMARY_LENGTH)
    privacy = models.IntegerField(default=0)

    # Meta information #

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"

        # TODO: ordering by created_at
        """
            ordering = ('created_at')
        """

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


################################################################################

class Story(models.Model):

    # Model constants #

    MAX_TITLE_LENGTH = 100

    # Attributes of Story model #

    activity = models.ForeignKey(Activity, related_name="stories")

    title = models.CharField(max_length=MAX_TITLE_LENGTH, default="")
    content = models.TextField()
    privacy = models.IntegerField(default=0)

    # TODO: make a storage for images and uploaded files and add array fields to Story model for files
    """
        image_files
        uploaded_files
    """

    # Meta information #

    class Meta:
        verbose_name = "story"
        verbose_name_plural = "stories"

        # TODO: ordering by created_at
        """
            ordering = ('created_at')
        """

    # Methods #

    def __str__(self):
        return self.title


################################################################################
