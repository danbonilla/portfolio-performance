from django.db import models

class Portfolios(models.Model):
	name = models.CharField(max_length=1024)

	def __unicode__(self):
		return unicode(self.name)

class PortfolioHistory(models.Model):
    portfolio_id = models.ForeignKey(Portfolios)
    date = models.DateField(blank=True)
    growth = models.FloatField(default=0)

    def __unicode__(self):
    	return unicode(self.portfolio_id)

class BenchmarkHistory(models.Model):
	date = models.DateField(blank=True)
	growth = models.FloatField(default=0)

	def __unicode__(self):
		return unicode(self.date)