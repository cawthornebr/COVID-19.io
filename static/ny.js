// Load data from hours-of-tv-watched.csv
console.log("test")

d3.csv("../data/new york_data/new york_master_file_total.csv").then(function(confirmedData) {
  // console.log(tvData)

  confirmedData.forEach(function(data) {

    var keys = Object.keys(data)
    var values = Object.values(data)

    // console.log(values[1])
    
    // Create the Trace
    var trace1 = [{
        x: keys,
        y: values,
        type: "bar"
      }];
      // console.log(data.Date)

    // Define the plot layout
    var layout = {
    title: "",
    xaxis: { title: "Date" },
    yaxis: { title: "Confirmed Cases" }
    };

    // Plot the chart to a div tag with id "bar-plot"
    Plotly.newPlot("plot", trace1, layout);

  });

}).catch(function(error) {
  console.log(error);
});