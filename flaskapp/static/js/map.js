

var mymap = L.map('map-id', {
  center: [-33.865143, 151.209900],
  zoom: 4
});


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoic3Vpc3VzcyIsImEiOiJja2pzMm53Mm0wMzh3MnJwZGhtZTh6MHI4In0.cDqyTTK6wlXvnfR342HdKA'
}).addTo(mymap);


// Create the createMarkers function 
function createMarkers(response) {

  // Loop through the stations array
  for (var i = 0; i < response.length; i++) {

    // For each station, create a marker and bind a popup with the IBRA region name
    var marker = L.marker([response[i]["lat"], response[i]["long"]]);
    marker.bindPopup(`<h1>${response[i]["IBRA Region Name"]}<h1><h2>% protected: ${response[i]["% IBRA Region Protected"]}</h2><h3>Total critically endangered: ${response[i]["total_ce"]}</h3>`);
    marker.addTo(mymap)
  }
}

var IBRAqueryUrl = "http://localhost/api/ibra";

d3.json(IBRAqueryUrl, createMarkers);

