from django.conf.urls import patterns, url, include
from rest_framework import routers
from .views import PortfolioView


router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'^api/portfolio/(?P<id>\w+)/?$', PortfolioView.as_view()),
    url(r'^$', include(router.urls)),
)
