from django.conf.urls import include, url
from .views import proxy_view

app_name = 'proxy'

urlpatterns = [
    url(r'^proxy/(?P<url>.*)$', proxy_view, name='proxy'),
]
