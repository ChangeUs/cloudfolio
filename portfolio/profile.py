
from portfolio.forms import *


class ProfileInfo:

    """
    Define profile information and form here
    """
    PROFILE = {
        'occupation': OccupationForm,
        'introduction': IntroductionForm,
        'birthday': BirthdayForm,
        'education': EducationForm,
    }

    @classmethod
    def get_profile_form(cls, title):
        if title not in cls.PROFILE:
            return None
        return cls.PROFILE[title]
