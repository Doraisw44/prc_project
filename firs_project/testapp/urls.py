
from django.conf.urls import url,include
from testapp import views

urlpatterns = [
    url(r'^$', views.base_view),
    url(r'^user/', views.user_register),
    url('accounts/', include('django.contrib.auth.urls')),
]
