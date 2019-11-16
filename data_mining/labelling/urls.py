from django.conf.urls import url, include

from .views import getAllLabels, home ,runCommand ,getOneLabel,update , run1,get1


urlpatterns = [
    url(r'^api/get-all', getAllLabels, name='getAllLabels'),
    url(r'^api/get1', get1, name='get1'),
    url(r'^api/get-one', getOneLabel, name='getOneLabel'),
    url(r'^api/update', update, name='update'),
    url(r'^api/run/$', runCommand, name='runCommand'),
    url(r'^api/run1/$', run1, name='run1'),
    url(r'^$', home, name='home'),
]
