from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url

from data_mining.labelling.urls import urlpatterns as labelling_url

urlpatterns = [
    url(r'^', include((labelling_url, 'labelling'), namespace='labelling')),
    path('admin/', admin.site.urls),
]
