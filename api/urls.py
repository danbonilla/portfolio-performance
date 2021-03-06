from django.conf.urls import patterns, url, include
from rest_framework import routers
from .views import PortfolioView, PortfolioListView, BenchmarkHistoryView, CumulativeReturnsView


router = routers.DefaultRouter()

urlpatterns = patterns('',
  url(r'^api/portfolios$', PortfolioListView.as_view()),
  url(r'^api/portfolio/(?P<id>\w+)/?$', PortfolioView.as_view()),
  url(r'^api/benchmark$', BenchmarkHistoryView.as_view()),
  url(r'^api/cumreturns/(?P<id>\w+)/?$',CumulativeReturnsView.as_view()),
  url(r'^$', include(router.urls)),
)
