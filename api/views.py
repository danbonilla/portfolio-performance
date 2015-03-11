from rest_framework import generics
<<<<<<< HEAD
from api.models import Portfolio, PortfolioHistory, BenchmarkHistory
from .serializers import PortfolioHistorySerializer
from .serializers import BenchmarkHistorySerializer
=======
from api.models import Portfolios, PortfolioHistory, BenchmarkHistory
from .serializers import PortfolioHistorySerializer, PortfoliosSerializer
>>>>>>> fe389936edc0343bb674d8542754b495e0ba8ad3


class PortfolioView(generics.ListAPIView):
    serializer_class = PortfolioHistorySerializer

    def get_queryset(self):
        portfolio_id = self.kwargs['id']
        fromdate = self.request.QUERY_PARAMS.get('fromdate', None)
        todate = self.request.QUERY_PARAMS.get('todate', None)
        if fromdate and todate: 

          query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).filter(date__range=[fromdate, todate]).order_by('-date')  

        elif fromdate: 
          query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).filter(date__gte=fromdate).order_by('-date')

        elif todate: 
          query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).filter(date__lte=todate).order_by('-date')

        else: 
          query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).order_by('-date')

        return query_set 

class BenchmarkHistoryView(generics.ListAPIView):
    serializer_class = BenchmarkHistorySerializer

    def get_queryset(self):
        fromdate = self.request.QUERY_PARAMS.get('fromdate', None)
        todate = self.request.QUERY_PARAMS.get('todate', None)
        if fromdate and todate: 

          query_set = BenchmarkHistory.objects.filter(portfolio_id=portfolio_id).filter(date__range=[fromdate, todate]).order_by('-date')    	
        return query_set

class PortfolioListView(generics.ListAPIView):
    serializer_class = PortfoliosSerializer

    def get_queryset(Self):
        query_set = Portfolios.objects.all()
        return query_set
