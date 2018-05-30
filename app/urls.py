from django.conf.urls import url
from django.contrib.auth import views as auth_views

from messenger import views as contact_v
from . import accounts as acc_views
from . import views


urlpatterns = [



    # NEW URLS
    url(r'^new-register/$', views.RegisterView_NEW, name='RegisterView'),

    url(r'^new-login/$', views.LoginView_NEW, name='LoginView'),

    url(r'^new-home/$', views.HomeView_NEW.as_view(), name='home'),

    url(r'^new-accounts/$', acc_views.AccountList_NEW.as_view(), name='accounts'),



    # OLD URLS

    # These are for user/page on our own
    url(r'^home/$', views.home),
    url(r'^newlanding/$', views.new_landing),
    url(r'^newauth/$', views.new_auth),
    url(r'^$', views.HomeView.as_view(), name='home'),

    # url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    # confirm email
    # change password
    # forgot passsword

    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(
            template_name='registration/logged_out.html',
             next_page='/'),
        name='logout'),
    url(r'^forgotpw',
        auth_views.PasswordResetView.as_view(
            template_name='registration/page-forgot-password.html'),
        name='forgotpw'),
    url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/page-password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'password_reset_complete',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/page-password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'password_reset_done',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/page-password_reset_done.html'),
        name='password_reset_done'),

    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^registered/$', views.TemplateView.as_view(
        template_name='registration/register_done.html'),
        name='register_done'),
    url(r'^subscription/$', views.SubsriptionView.as_view(), name='subscription'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.ActivateAccount.as_view(), name='activate'),

    # these stuff will be for account on linkedIN
    url(r'^accounts/$', acc_views.AccountList.as_view(), name='accounts'),
    url(r'^accounts/info/$', acc_views.AccountInfo.as_view(), name='account-info'),
    url(r'^account/(?P<pk>[\d]+)/$', acc_views.AccountDetail.as_view(), name='account-detail'),
    url(r'^accounts/(?P<pk>[\d]+)/settings/$', acc_views.AccountSettings.as_view(), name='account-settings'),
    url(r'^accounts/add/$', acc_views.AccountAdd.as_view(), name='add-account'),
    url(r'^accounts/remove/(?P<pk>[\d]+)$', acc_views.RemoveAccount.as_view(),
        name = 'remove-account'),
    # url(r'^accounts/pinverify/(?P<pk>[\d]+)$', acc_views.update_account, name='pinverify'),

    url(r'^account/(?P<pk>[\d]+)/network/$',
        acc_views.AccountNetwork.as_view(), name='account-network'),
    url(r'^account/(?P<pk>[\d]+)/messenger/$',
        acc_views.AccounMessenger.as_view(), name='account-messenger'),
    url(r'^account/(?P<pk>[\d]+)/campaigns/$',
        acc_views.AccountCampaign.as_view(), name='account-campaign'),
    url(r'^account/(?P<pk>[\d]+)/search/$',
        acc_views.AccountSearch.as_view(), name='account-search'),
    url(r'^account/(?P<pk>[\d]+)/search/delete/(?P<search_id>[\d]+)/$',
        acc_views.AccountSearchDelete.as_view(), name='account-search-delete'),
    url(r'^accounts/search_result/$', acc_views.SearchResultView.as_view(),
        name='account-search-result'),
    url(r'^account/(?P<pk>[\d]+)/all/$',
        acc_views.AccountInbox.as_view(), name='account-all'),
    url(r'^account/(?P<pk>[\d]+)/tasks/$',
        acc_views.AccountTask.as_view(), name='account-task'),
    url(r'^account/(?P<pk>[\d]+)/messenger/add$',
        acc_views.AccountMessengerCreate.as_view(), name='account-messenger-add'),
    url(r'^account/(?P<pk>[\d]+)/campaigns/add$',
        acc_views.AccountCampaignCreate.as_view(), name='account-campaign-add'),
    url(r'^account/messenger/(?P<pk>[\d]+)$',
        acc_views.AccountMessengerDetail.as_view(), name='messenger-campaign'),
    url(r'^account/campaigns/(?P<pk>[\d]+)$',
        acc_views.AccountCampaignDetail.as_view(), name='connector-campaign'),
    url(r'^account/bottask/(?P<pk>[\d]+)$',
        acc_views.AccountBotTask.as_view(), name='bottask'),

    url(r'^account/messenger/(?P<pk>[\d]+)/delete$',
        acc_views.AccountMessengerDelete.as_view(), name='messenger-campaign-delete'),
    url(r'^account/campaigns/(?P<pk>[\d]+)/delete$',
        acc_views.AccountMessengerDelete.as_view(), name='connector-campaign-delete'),
    url(r'^account/campaigns/(?P<pk>[\d]+)/active',
        acc_views.AccountMessengerActive.as_view(), name='connector-campaign-active'),
    url(r'^account/messenger/(?P<pk>[\d]+)/active',
        acc_views.AccountMessengerActive.as_view(), name='messenger-campaign-active'),
    url(r'^account/contact/(?P<pk>[\d]+)/status', contact_v.ContactStatusView.as_view(),
        name='contact-status')
]
