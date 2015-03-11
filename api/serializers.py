from rest_framework import serializers
from api.models import Portfolios, PortfolioHistory, BenchmarkHistory

class PortfoliosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolios
        fields = ('id', 'name')

class PortfolioHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioHistory
        fields = ('date', 'growth')

class BenchmarkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkHistory
        fields = ('date', 'growth')