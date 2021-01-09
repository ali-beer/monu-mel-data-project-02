var ausCoords = [-25.2744, 133.7751];
var mapZoomLevel = 12;


// Create the createMap function
function createMap(ibraRegion) {
  
  // Create the tile layer that will be the background of our map
  var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'});
  
  var topomap = L.tileLayer('https://{a|b|c}.tile.opentopomap.org/{z}/{x}/{y}.png', {foo: 'bar', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'});
  


  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = { // javascript object
    "Street Map": streetmap,
    "Light Map": topomap
  }

  // Create an overlayMaps object to hold the IBRA Region layer
  var overlayMaps = {
    "IBRA Region Name": ibraRegion
  }

  // Create the map object with options
  var map = L.map("map-id", { // 1st parameter is the id of the
  // html div element where you want your map to appear
    center: ausCoords, // lat, lon pair for where you want the map to be
    zoom: mapZoomLevel,
    layers: [streetmap, ibraRegion]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. 
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, { // L.control - Leaflet gives us a handy way of creating controls on our map
    collapsed: false
  }).addTo(map);
}



// Create the createMarkers function
function createMarkers(response) {
  console.log("createMarkers");

  console.log(response);

  // Initialize an array to hold IBRA region markers
  var markers = [];

  // Loop through the stations array
  for (var i = 0; i < response.length; i++) {
 

    // For each station, create a marker and bind a popup with the IBRA region name
    var marker = L.marker([response.latitude, response.longitude]);
    marker.bindPopup(`<h1>${response["IBRA Region Name"]}<h1><h2>% protected: ${response["% IBRA Region Protected"]}</h2><h3>Total critically endangered: ${response["total_ce"]}</h3>`);

    // Add the marker to the IBRA region markers array
    markers.push(marker);
  }

  // Create a layer group made from the markers array
  // pass it into the createMap function
  createMap(L.layerGroup(markers));
}

// Perform an API call to the local host port 5000 API to get information. Call createMarkers when complete
var queryUrl = "port5000/localhost/API/IBRA";

d3.json(queryUrl, createMarkers);

// d3.json(queryUrl, function(data) {
//   console.log(data);
// });