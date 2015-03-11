from rest_framework import generics
from api.models import Portfolio, PortfolioHistory, BenchmarkHistory
from .serializers import PortfolioHistorySerializer


class PortfolioView(generics.ListAPIView):
    serializer_class = PortfolioHistorySerializer

    def get_queryset(self):
        portfolio_id = self.kwargs['id']
        # logged_in_user = self.request.QUERY_PARAMS.get('logged_in_user', None)

    	query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).order_by('-month')  	
        return query_set