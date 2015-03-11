from django.db import models

class Portfolio(models.Model):
	name = models.CharField(max_length=1024)

	def __unicode__(self):
		return unicode(self.name)

class PortfolioHistory(models.Model):
    portfolio_id = models.ForeignKey(Portfolio)
    month = models.DateField(blank=True)
    growth = models.IntegerField(default=0)

    def __unicode__(self):
    	return unicode(self.portfolio_id)

class BenchmarkHistory(models.Model):
	month = models.DateField(blank=True)
	growth = models.IntegerField(default=0)

	def __unicode__(self):
		return unicode(self.month)