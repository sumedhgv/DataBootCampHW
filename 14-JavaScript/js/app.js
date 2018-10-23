// from data.js
var tableData = data;

//var tbody = d3.select('tbody');

// interate through each info in the order of:
// datetime, city, state, country, shape, duration, comments
tableData.forEach( sighting => {
    var row = tbody.append('tr');
    row.append("td").text(sighting.datetime);
    row.append("td").text(sighting.city);
    row.append("td").text(sighting.state);
    row.append("td").text(sighting.country);
    row.append("td").text(sighting.shape);
    row.append("td").text(sighting.durationMinutes);
    row.append("td").text(sighting.comments);
});

// ----------------------------------------------------------------------------
// - Use a date form in the HTML document and write JavaScript code that will
//   listen for events and search through the datetime column to find rows that 
//   match user input.
// ----------------------------------------------------------------------------
var submitbtn = d3.select("#filter-btn")

submitbtn.on("click", function() {
    // prevent the page from refreshing
    d3.event.preventDefault();

    // select the input element and get the value
    var input = d3.select('#datetime');
    var inputValue = input.property('value');

    // use the form input to filter the event
    if (inputValue) {
        var eventfilter = tableData.filter(event => event.datetime === inputValue);
    } else {
        var eventfilter = tableData;
    };

    // clean previous table
    d3.selectAll('tbody > tr').remove();

    // append event on the specific datetime to the table
    eventfilter.forEach( event => {
        row2 = tbody.append('tr');
        row2.append("td").text(event.datetime);
        row2.append("td").text(event.city);
        row2.append("td").text(event.state);
        row2.append("td").text(event.country);
        row2.append("td").text(event.shape);
        row2.append("td").text(event.durationMinutes);
        row2.append("td").text(event.comments);
    });
});
