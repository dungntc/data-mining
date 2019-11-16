from django.conf.urls import url, include

from .views import getAllLabels


urlpatterns = [
    url(r'^$', getAllLabels, name='getAllLabels'),
]
