from django.conf.urls import url

from .views import logout


urlpatterns = [
    url(r'^logout/$', logout)
]
