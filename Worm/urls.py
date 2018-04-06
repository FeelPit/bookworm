from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^start/$',  views.start),
    url(r'^steve_jobs/$', views.user_login_view),
    url(r'^test/$', views.user_login_view),
    url(r'^reg/$', views.registration),
    url(r'^log/$', views.login_up)
]