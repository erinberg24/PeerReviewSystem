

document.querySelector("#ranking-type").addEventListener("change", updateBarChart);
document.querySelector("#name-group-type").addEventListener("change", updateBarChart);

function updateBarChart(){
  let column = document.querySelector("#ranking-type").value;
  let name = document.querySelector("#name-group-type").value;
  console.log(column);
  let spec = {
    $schema: "https://vega.github.io/schema/vega-lite/v4.json",
    width: 400,
    height: 300,
    description: "A simple bar chart with embedded data.",
    data: {url: "./data/"+name+"assessmentResults.csv"},
    mark: {
      "type": "line",
      "point": true
    },
    encoding: {
      x: {field: "Week", type: "quantitative", text: {angle:"90"}},
      y: {field: column, type: "quantitative", axis: {title: column + " Score"}}
    }
  };
  vegaEmbed('#chart-area', spec);
}

updateBarChart();