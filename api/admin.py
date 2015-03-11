from django.contrib import admin
from api.models import Portfolios, PortfolioHistory, BenchmarkHistory

class PortfolioHistoryAdmin(admin.ModelAdmin):
    list_display = ('portfolio_id', 'date', 'growth')

admin.site.register(Portfolios)
admin.site.register(PortfolioHistory, PortfolioHistoryAdmin)
admin.site.register(BenchmarkHistory)
