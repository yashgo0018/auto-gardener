var endpoint = '/api/data/';
var chart_data;
$.ajax({
    method: "GET",
    url: endpoint,
    success: (data) => {
        chart_data = data;
    },
    error: (error) => {
        console.log(error)
    }
})
function get_final_data(data) {
    var chart_data_final = []
    for(i=0; i<data.length;i++){
        var [datetime, temperature, humidity, moisture] = chart_data[i];
        var [date, time] = datetime.split(' ')
        var [hour, min, sec] = time.split(':');
        var [year, month, day] = date.split('-');
        datetime =  new Date(year, month-1, day, hour, min, sec);
        chart_data_final.push([datetime, temperature, humidity, moisture]);
    }
    return chart_data_final
}
google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawCurveTypes);

function drawCurveTypes() {
    var data = new google.visualization.DataTable();
    data.addColumn('datetime', 'X');
    data.addColumn('number', 'Temperature');
    data.addColumn('number', 'Humidity');
    data.addColumn('number', 'Moisture');
    data.addRows(get_final_data(chart_data));

    var options = {
        hAxis: {
        title: 'Time'
        },
        series: {
        1: {curveType: 'function'}
        }
    };
    var chart_div = document.getElementById('chart_div')
    var chart = new google.visualization.LineChart(chart_div);
    chart.draw(data, options);
}