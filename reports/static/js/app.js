(function($) {

	$(document).ready(function() {
    var portfolioSelectContainer = $("#portfolio-select");
    var portfoliosUrl = "/api/portfolios";
    var chart = performanceChart({ svg: '#chart svg' });

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
      var checkboxes = $('#portfolio-select input[type="checkbox"]');
      var seriesDataPromise = chart.loadData(checkboxes);

      seriesDataPromise.done(function(seriesData) {
        chart.showData(seriesData);
      });
    });
    
  });
})(jQuery);