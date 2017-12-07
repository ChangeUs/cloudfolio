from django.test import TestCase
from account.models import *
from portfolio.models import *

# Create your tests here.

user = Account(
    name='강하늘',
    email='kang@changeus.com'
)

user.set_password('1234')
user.is_active = True
user.is_staff = True
user.is_superuser = True

user.save()

portfolio = Portfolio.make_portfolio(user)
profile = portfolio.profile

profile.profile = {'address': {'public': True, 'residence': '서울', 'active_area': '서울시 강동구'},
                   'contact': {'public': True, 'phone_number': '02-3426-1111', 'mobile_phone_number': '010-1010-0303'},
                   'homepage': {'public': True, 'blog_page': 'http://blog.naver.com/kcs0630',
                                'github_page': 'http://www.github.com/Kim-Chul-Su',
                                'behance_page': '', 'twitter_page': '', 'facebook_page': '',
                                'linkedin_page': '', 'instagram_page': ''},
                   'language': [{'level': '3', 'public': True, 'language_name': '영어'},
                                {'level': '2', 'public': True, 'language_name': '일본어'}],
                   'education': [{'major': '정보통신과', 'degree': '', 'public': True,
                                  'school': '선린인터넷고등학교', 'end_date': None, 'in_school': False, 'start_date': None},
                                 {'major': '컴퓨터공학과', 'degree': '학사', 'public': True, 'school': '서울대학교',
                                  'end_date': None, 'in_school': True, 'start_date': None}],
                   'occupation': {'public': True, 'occupation': '웹 개발'},
                   'introduction': {'public': True, 'introduction': '안녕하세요! 웹 개발 쪽 프리랜서로 일하고 있습니다!!'},
                   'interest_keyword': [{'public': True, 'interest_keyword': '웹 개발'},
                                        {'public': True, 'interest_keyword': 'Front-end'},
                                        {'public': True, 'interest_keyword': 'Back-end'},
                                        {'public': True, 'interest_keyword': 'django'},
                                        {'public': True, 'interest_keyword': 'AngularJS'},
                                        {'public': True, 'interest_keyword': 'Python'},
                                        {'public': True, 'interest_keyword': 'C++'},
                                        {'public': True, 'interest_keyword': 'java'},
                                        {'public': True, 'interest_keyword': 'javascript'}]}

profile.save()

award = portfolio.make_tab('수상이력')

activity1 = award.make_activity('ACM-ICPC 전세계 본선 진출', '전세계 대학생을 주관으로 하는 알고리즘 대회인 ACM-ICPC 대회에 본선 진출하였다. ', privacy=PrivacyModel.PUBLIC_ALL)

activity1.make_story('ACM-ICPC 전세계 본선', '<img src="https://www.google.co.kr/url?sa=i&rct=j&q=&esrc=s'
                                        '&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjzk-Cvm4nXAhXEWbw'
                                        'KHYALBosQjRwIBw&url=http%3A%2F%2Fwww.icpc2014.ru%2F&psig=AOvVaw19'
                                        'Z0VgMf3BPVrCCV6d9EG6&ust=1508932934499886">', privacy=PrivacyModel.PUBLIC_ALL)

project = portfolio.make_tab('진행했던 프로젝트')

activity2 = project.make_activity('교내 앱 제작', '교내에서 학교와 관련된 정보를 제공하고 정보를 공유하여 학생들이 유용하게 사용할 수 있는 어플리케이션을 제작하였다.', privacy=PrivacyModel.PUBLIC_ALL)

activity2.make_story('수요 조사', '''교내에서 학생들이 학교 생활을 하
면서 어떤 점이 불편한지에 대해 알아보기로 하였다. 온라인으로는 학교 커뮤니티 사
이트, 오프라인 상으로는 주변 지인들을 통해서 불편한 점을 알아보았다. 그 결과 학
교 급식 메뉴를 쉽게 볼 수 있었으면 좋겠다, 교수님에 대한 평이 있었으면 좋겠다, 
학교 안에 있는 숨겨진 장소(맛집, 포탈) 등에 대한 정보를 공유할 수 있었으면 좋겠
다 등의 의견을 수렴받을 수 있었다.''', privacy=PrivacyModel.PUBLIC_ALL)



project.make_activity('교내 저작권 홈페이지 제작 대회 장려상', '교내(선린인터넷고등학교)에서 진행한 저작권 홈페이지 제작 대회에서 장려상을 수상하였다. ', privacy=PrivacyModel.PUBLIC_ALL)
