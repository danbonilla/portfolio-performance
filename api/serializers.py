from rest_framework import serializers
from api.models import Portfolio, PortfolioHistory, BenchmarkHistory

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('name')

class PortfolioHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioHistory
        fields = ('date', 'growth')

class BenchmarkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkHistory
        fields = ('date', 'growth')