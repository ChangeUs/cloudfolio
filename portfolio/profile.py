
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
        'contact': ContactForm,
        'address': AddressForm,
        'interest_keyword': InterestKeywordsForm,
        'homepage': HomepageForm,
        'certificate': CertificateForm,
        'language': LanguageForm,
        'technology': TechnologyForm,
    }

    @classmethod
    def get_profile_form(cls, title):
        if title not in cls.PROFILE:
            return None
        return cls.PROFILE[title]
