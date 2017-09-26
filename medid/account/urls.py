from django.conf.urls import url,include
from . import views
#Default url patterns existing
urlpatterns=[
    url(r'^$',views.index),
    url(r'^signup$',views.trial),
    url(r'^profile_doc$',views.profile_doc),
    url(r'^scan_doc$',views.scan_doc),
    url(r'^doc_view_presc',views.doc_view_presc),
    url(r'^doc_presc_new',views.doc_presc_new),
    url(r'^report_doc',views.report_doc),
    url(r'^doc_view$',views.doc_view),
    url(r'^profile_user$',views.patientpage),
    url(r'^prescriptions_user$',views.prescriptions_user),
    url(r'^report_user$',views.report_user),
    url(r'^profile_pharm$',views.profile_pharm),
    url(r'^scand$',views.scand),
    url(r'^login',views.login),
    url(r'^login_doc$',views.login_doc),
    url(r'^login_phar$',views.login_phar)
]
