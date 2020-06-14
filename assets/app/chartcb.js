
$(document).ready(function(){

    var $populationChart = $("#cb-chart");
    $.ajax({
        url: $populationChart.data("url"),
        success: function (data) {

            var ctx = $populationChart[0].getContext("2d");

            console.log(ctx)

            new Chart(ctx, {
                type: 'bar',
                data: {
                  labels: data.labels,
                  datasets: [
                      {
                        label: 'Hasil Prediksi',
                        data: data.data1,
                        backgroundColor: 'blue'
                      },
                      {
                        label: 'Data Aktual',
                        data: data.data2,
                        backgroundColor: 'orange'
                      }
                  ]
                },
                options: {
                  responsive: true,
                  legend: {
                    position: 'top',
                  },
                  scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            stepSize: 5
                        }
                    }]
                }
                }
              });
        }
    });

});