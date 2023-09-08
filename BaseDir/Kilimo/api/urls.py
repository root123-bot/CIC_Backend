from django.urls import path
from django.conf.urls import url
from Kilimo.register.views import *
from django.views.generic import TemplateView
from Kilimo.main.views import *

urlpatterns = [
    url(r'draftarticle/$', draft_article, name="draftarticle"),
    url(r'updatearticle/$', update_article, name="updatearticle"),
    url(r'officerposts/$', officer_posts, name="officerposts"),
    url(r'rarticleslist/$', articles_list, name="rarticleslist"),
    url(r'rarticles/$', r_articles, name="rarticles"),
    url(r'createarticle/$', create_article, name="createarticle"),
    url(r'completeofficerprofile/$', complete_officer_profile, name="completeofficerprofile"),
    url(r'completeresearcherprofile/$', complete_researcher_profile, name="completeresearcherprofile"),
    url(r'delete_user/$', delete_user, name='deleteuser'),
    url(r'userdetails/$', user_details, name='userdetails'),
    url(r'login/$', login, name='login_user'),
    url(r'register/$', register_user, name='register_user'),
    url(r'isuserexist/$', is_user_exist, name='isuserexist'),
    url(r'sendotp/$', send_otp, name="sendotp"),
    url(r'validateotp/$', validate_otp, name='validateotp'),
]
