from django.conf.urls import url, include

from .views import getAllLabels, home ,runCommand ,getOneLabel,update , runSelect3


urlpatterns = [
    url(r'^api/get-all', getAllLabels, name='getAllLabels'),
    url(r'^api/get-one', getOneLabel, name='getOneLabel'),
    url(r'^api/update', update, name='update'),
    url(r'^api/run/$', runCommand, name='runCommand'),
    url(r'^api/run1/$', runSelect3, name='runSelect3'),
    url(r'^$', home, name='home'),
]
