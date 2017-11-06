
from portfolio.forms import *


class TeamProfileInfo:

    """
    Define profile information and form here
    """
    PROFILE = {
        'team-introduction': TeamIntroductionForm, #기업 소개글
        'team-establishment': TeamEstablishment, #설립일
        'team-address': TeamAddressForm, #사무실 주소
        'team-contact': TeamContactForm, #연락처
        'team-ceo': TeamCEOForm, #CEO 정보
        'team-members': TeamMemberForm, #팀원 정보
        'team-homepage': HomepageForm, #각종 SNS
        'team-news': TeamNewsForm, #관련 뉴스기사
        'team-related-keyword': RelatedKeywordsForm, #관련 키워드
        'team-desired-talent': DesiredTalentForm, #원하는 인재상
    }

    @classmethod
    def get_profile_form(cls, title):
        if title not in cls.PROFILE:
            return None
        return cls.PROFILE[title]
