(function($) {

/* Inspired by Lee Byron's test data generator. */
function stream_layers(n, m, o) {
  if (arguments.length < 3) o = 0;
  function bump(a) {
    var x = 1 / (.1 + Math.random()),
        y = 2 * Math.random() - .5,
        z = 10 / (.1 + Math.random());
    for (var i = 0; i < m; i++) {
      var w = (i / m - y) * z;
      a[i] += x * Math.exp(-w * w);
    }
  }
  return d3.range(n).map(function() {
      var a = [], i;
      for (i = 0; i < m; i++) a[i] = o + o * Math.random();
      for (i = 0; i < 5; i++) bump(a);
      return a.map(stream_index);
    });
}

/* Another layer generator using gamma distributions. */
function stream_waves(n, m) {
  return d3.range(n).map(function(i) {
    return d3.range(m).map(function(j) {
        var x = 20 * j / m - i / 3;
        return 2 * x * Math.exp(-.5 * x);
      }).map(stream_index);
    });
}

function stream_index(d, i) {
  return {x: i, y: Math.max(0, d)};
}

	$(document).ready(function() {
    var portfolioSelectContainer = $("#portfolio-select");
    var portfoliosUrl = "/api/portfolios";

    var portfoliosPromise = $.ajax({
          type: "GET",
          url: portfoliosUrl,
          dataType: 'json', 
          contentType: 'application/json; charset=UTF-8'
      });

    portfoliosPromise.done(function(data) {
      _.each(data, function(portfolio) {
        var checkbox = $('<input type="checkbox" value="' + portfolio.id + '" name="' + portfolio.name +'"/><label> ' + portfolio.name + '</label></br>');
        portfolioSelectContainer.append(checkbox);
      });
    });

    $('#report-submit').on("click", function() {
      var portfolios = [];
      var portfolioPromises = [];
      var portfolioSeries = [];

      var checkboxes = $('#portfolio-select input[type="checkbox"]');
      _.each(checkboxes, function(checkbox) {
        if (checkbox.checked) {
          portfolios.push({ name: $(checkbox).attr("name"), value: checkbox.value});
        }
      });

      var benchmarkPromise = $.ajax({
          type: "GET",
          url: "/api/benchmark?fromdate=" + $('#fromdate').val() + "&todate=" + $('#todate').val(),
          dataType: 'json', 
          contentType: 'application/json; charset=UTF-8'
        });

      portfolioPromises.push(benchmarkPromise);

      _.each(portfolios, function(portfolio) {
        var performancePromise = $.ajax({
          type: "GET",
          url: "/api/portfolio/" + portfolio.value +"?fromdate=" + $('#fromdate').val() + "&todate=" + $('#todate').val(),
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
        console.log(seriesData);
        chartOurData(seriesData);
      });

      function mapPerformanceDataToSeries(isBenchmark, seriesData) {
        var chartData = [];
        var lastData = null;
        var benchmarkSum = 0;
        _.each(seriesData, function(data) {
          var value;
          if (isBenchmark) {
            var change = lastData !== null ? (data.growth/lastData.growth) - 1 : 0;
            console.log(change);
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
    });


    function chartOurData(series) {
      nv.addGraph(function() {
        var chart = nv.models.lineWithFocusChart();

        chart.xAxis.tickFormat(function(d) {
          var date = new Date(0);
          date.setUTCSeconds(d);
          return d3.time.format('%b %y')(new Date(date))
        });

        chart.yAxis
            .tickFormat(d3.format(',.2f'));

        chart.y2Axis
            .tickFormat(d3.format(',.2f'));

        d3.select('#chart svg')
            .datum(series)
            .transition().duration(500)
            .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
      });

    }

    /**************************************
     * Simple test data generator
     */

    function testData() {
      return stream_layers(3,128,.1).map(function(data, i) {
        return { 
          key: 'Stream' + i,
          values: data
        };
      });
    }

	});
})(jQuery);