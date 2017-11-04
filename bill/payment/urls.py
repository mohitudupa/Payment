from django.conf.urls import url
from . import views

app_name = 'payment'

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^(?P<aadhar_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^user/login/$', views.user_login, name='user_login'),
    url(r'^user/bills/$', views.detail1, name='detail1'),
    url(r'^user/logout/$', views.user_logout, name='user_logout'),
    url(r'^company/login/$', views.company_login, name='company_login'),
    url(r'^company/bills/$', views.company_detail, name='company_detail'),
    url(r'^company/bills/(?P<bill_id>[0-9]+)/$', views.due_bill, name='due_bill'),
    url(r'^register/$', views.register, name='register'),
    url(r'^upload/$', views.upload, name='upload'),
    # url(r'^company/logout/$', views.company_logout, name='company_logout')
    # url(r'^pdf/$', views.HelloPDFView.as_view(), name='pdf'),
    url(r'^gen/$', views.gen, name='gen'),
    url(r'^user/change_password/$', views.user_change_password, name='user_change_password'),
    url(r'^company/change_password/$', views.company_change_password, name='company_change_password'),
    url(r'^burner/$', views.burner, name='burner')
]
