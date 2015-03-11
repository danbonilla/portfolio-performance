from django.contrib import admin
from api.models import Portfolio, PortfolioHistory, BenchmarkHistory


admin.site.register(Portfolio)
admin.site.register(PortfolioHistory)
admin.site.register(BenchmarkHistory)
