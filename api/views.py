from rest_framework import generics
from api.models import Portfolio, PortfolioHistory, BenchmarkHistory
from .serializers import PortfolioHistorySerializer


class PortfolioView(generics.ListAPIView):
    serializer_class = PortfolioHistorySerializer

    def get_queryset(self):
        portfolio_id = self.kwargs['id']
        fromdate = self.request.QUERY_PARAMS.get('fromdate', None)
        todate = self.request.QUERY_PARAMS.get('todate', None)

    	query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).filter(date__range=[fromdate, todate]).order_by('-date')  	
        return query_set