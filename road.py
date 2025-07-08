<!DOCTYPE html>
<html>
<head>
  <title>India Highways Map</title>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
  <style>
    #map { height: 100vh; margin:0; }
  </style>
</head>
<body>
  <div id="map"></div>
  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
  <script>
    var map = L.map('map').setView([20.6, 78.9], 5); // Center on India

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    fetch('india_highways.geojson') // contains NH polylines & codes
      .then(r => r.json())
      .then(data => {
        L.geoJson(data, {
          style: feature => ({
            color: feature.properties.number.startsWith('NH-') ? 'red' : 'blue',
            weight: 3
          }),
          onEachFeature: (f, layer) => {
            layer.bindPopup(f.properties.number);
          }
        }).addTo(map);
      });
  </script>
</body>
</html>
