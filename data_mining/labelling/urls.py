from django.conf.urls import url, include

from .views import getAllLabels, home ,runCommand ,getOneLabel


urlpatterns = [
    url(r'^api/get-all', getAllLabels, name='getAllLabels'),
    url(r'^api/get-one', getOneLabel, name='getOneLabel'),
    url(r'^api/run/$', runCommand, name='runCommand'),
    url(r'^$', home, name='home'),
]
