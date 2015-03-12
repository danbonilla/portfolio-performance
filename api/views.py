from rest_framework import generics
from api.models import Portfolios, PortfolioHistory, BenchmarkHistory
from .serializers import PortfolioHistorySerializer, PortfoliosSerializer, BenchmarkHistorySerializer, CumulativeReturnsSerializer


class PortfolioView(generics.ListAPIView):
    serializer_class = PortfolioHistorySerializer

    def get_queryset(self):
        portfolio_id = self.kwargs['id']
        fromdate = self.request.QUERY_PARAMS.get('fromdate', None)
        todate = self.request.QUERY_PARAMS.get('todate', None)
        if fromdate and todate: 
            query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).filter(date__range=[fromdate, todate]).order_by('date')  
        elif fromdate: 
            query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).filter(date__gte=fromdate).order_by('date')
        elif todate: 
            query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).filter(date__lte=todate).order_by('date')
        else: 
            query_set = PortfolioHistory.objects.filter(portfolio_id=portfolio_id).order_by('date')

        return query_set 

class BenchmarkHistoryView(generics.ListAPIView):
    serializer_class = BenchmarkHistorySerializer

    def get_queryset(self):
        fromdate = self.request.QUERY_PARAMS.get('fromdate', None)
        todate = self.request.QUERY_PARAMS.get('todate', None)
        if fromdate and todate: 
            query_set = BenchmarkHistory.objects.filter(date__range=[fromdate, todate]).order_by('date')  
        elif fromdate: 
            query_set = BenchmarkHistory.objects.filter(date__gte=fromdate).order_by('date')
        elif todate:
            query_set = BenchmarkHistory.objects.filter(date__lte=todate).order_by('date')
        else:
            query_set = BenchmarkHistory.objects.all().order_by('date')      	
          
        return query_set

class PortfolioListView(generics.ListAPIView):
    serializer_class = PortfoliosSerializer

    def get_queryset(self):
        query_set = Portfolios.objects.all()
        return query_set

class CumulativeReturnsView(generics.ListAPIView):
    serializer_class = CumulativeReturnsSerializer

    def get_queryset(self):
        portfolio_id = self.kwargs['id']
        fromdate = self.request.QUERY_PARAMS.get('fromdate', None)
        todate = self.request.QUERY_PARAMS.get('todate', None)

        if fromdate and todate:
            fromdate = fromdate[0:7]
            todate = todate[0:7]
            fromgrowth = PortfolioHistory.objects.values_list('growth').get(portfolio_id=portfolio_id, date__contains=fromdate)
            torowth = PortfolioHistory.objects.values_list('growth').get(portfolio_id=portfolio_id, date__contains=todate)

            frombm = BenchmarkHistory.objects.values_list('growth').get(date__contains=fromdate)
            tobm = BenchmarkHistory.objects.values_list('growth').get(date__contains=todate)

        elif fromdate: 
            fromdate = fromdate[0:7]
            fromgrowth = PortfolioHistory.objects.values_list('growth').get(portfolio_id=portfolio_id, date__contains=fromdate)
            torowth = PortfolioHistory.objects.values_list('growth').filter(portfolio_id=portfolio_id).order_by('-date')[0]

            frombm = BenchmarkHistory.objects.values_list('growth').get(date__contains=fromdate)
            tobm = BenchmarkHistory.objects.values_list('growth').order_by('-date')[0]

        elif todate:
            todate = todate[0:7]
            fromgrowth = PortfolioHistory.objects.values_list('growth').filter(portfolio_id=portfolio_id).order_by('date')[0]
            torowth = PortfolioHistory.objects.values_list('growth').get(portfolio_id=portfolio_id, date__contains=todate)

            frombm = BenchmarkHistory.objects.values_list('growth').order_by('date')[0]
            tobm = BenchmarkHistory.objects.values_list('growth').get(date__contains=todate)

        else:
            fromgrowth = PortfolioHistory.objects.values_list('growth').filter(portfolio_id=portfolio_id).order_by('date')[0]
            torowth = PortfolioHistory.objects.values_list('growth').filter(portfolio_id=portfolio_id).order_by('-date')[0]
            
            frombm = BenchmarkHistory.objects.values_list('growth').order_by('date')[0]
            tobm = BenchmarkHistory.objects.values_list('growth').order_by('-date')[0]

        fgvalue = 1+(fromgrowth[0]/100)
        tgvalue = 1+(torowth[0]/100)
        pTWRR = ((tgvalue/fgvalue)-1)*100
        bTWRR = ((tobm[0]/frombm[0])-1)*100

        data = [{'portfolio':pTWRR, 'benchmark': bTWRR}]
        return data

