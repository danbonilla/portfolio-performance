var performanceChart = function(options) {
	var settings = $.extend({
        svg: "#chart svg",
        startDate: null,
        endDate: null
    }, options);

  var startDateInput = $(settings.startDate);
  var endDateInput = $(settings.endDate);

  function loadDataForCheckedPortfolios(checkboxes) {
    var portfolios = [];
    var portfolioPromises = [];
    var portfolioSeries = [];
    var seriesDeferred = jQuery.Deferred();
    var queryString = "";

    if (startDateInput.val()) {
      queryString += queryString ? "&" : "?";
      queryString += "fromdate=" + startDateInput.val();
    }

    if (endDateInput.val()) {
      queryString += queryString ? "&" : "?";
      queryString += "todate=" + endDateInput.val();
    }

    _.each(checkboxes, function(checkbox) {
      if (checkbox.checked) {
        portfolios.push({ name: $(checkbox).attr("name"), value: checkbox.value});
      }
    });

    var benchmarkPromise = $.ajax({
        type: "GET",
        url: "/api/benchmark" + queryString,
        dataType: 'json', 
        contentType: 'application/json; charset=UTF-8'
      });

    portfolioPromises.push(benchmarkPromise);

    _.each(portfolios, function(portfolio) {
      var performancePromise = $.ajax({
        type: "GET",
        url: "/api/portfolio/" + portfolio.value + queryString,
        dataType: 'json', 
        contentType: 'application/json; charset=UTF-8'
      });
      portfolioPromises.push(performancePromise);
    })

    $.when.apply($, portfolioPromises).then(function() {
      var seriesData = [];
      var key, chartData;
      var results = arguments;
      for (var i = 0; i < results.length; i++) {
        chartData = mapPerformanceDataToSeries(i === 0, results[i][0]);
        key = i === 0 ? "benchmark" : portfolios[i-1].name;
        seriesData.push({ key: key, values: chartData });
      }
      //console.log(seriesData);
      return seriesDeferred.resolve(seriesData);
    });

    return seriesDeferred.promise();
  }

  function mapPerformanceDataToSeries(isBenchmark, seriesData) {
    var chartData = [];
    var lastData = null;
    var benchmarkSum = 0;
    _.each(seriesData, function(data) {
      var value;
      if (isBenchmark) {
        var change = lastData !== null ? (data.growth/lastData.growth) - 1 : 0;
        benchmarkSum += change * 100;
        value = benchmarkSum;
      }
      else {
        value = data.growth;
      }
      chartData.push({ x: new Date(data.date).getTime() / 1000, y: value });
      lastData = data;
    });
    return chartData;
  }

  function showSeriesData(series) {
    nv.addGraph(function() {
      var chart = nv.models.lineWithFocusChart();

      chart.xAxis.tickFormat(function(d) {
        var date = new Date(0);
        date.setUTCSeconds(d);
        return d3.time.format('%b %y')(new Date(date))
      });

      chart.x2Axis.tickFormat(function(d) {
        var date = new Date(0);
        date.setUTCSeconds(d);
        return d3.time.format('%b %y')(new Date(date))
      });

      chart.yAxis
          .tickFormat(d3.format(',.2f'));

      chart.y2Axis
          .tickFormat(d3.format(',.2f'));

      d3.select(settings.svg)
          .datum(series)
          .transition().duration(500)
          .call(chart);

      nv.utils.windowResize(chart.update);

      return chart;
    });
  }

  return {
		showData: showSeriesData,
    loadData: loadDataForCheckedPortfolios
	};
};
