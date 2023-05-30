<?php
if (isset($_GET['lat']) && isset($_GET['lng'])) {
  $latitude = $_GET['lat'];
  $longitude = $_GET['lng'];
  
  // Save location details to file
  $file = fopen("location.txt", "a");
  fwrite($file, "Latitude: " . $latitude . ", Longitude: " . $longitude . "\n");
  fclose($file);
}
?>

<!DOCTYPE html>
<html>
<head>
  <title>Another Page</title>
  <style>
    body {
      text-align: center;
      margin-top: 200px;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Location Saved!</h1>
  <p>Location details have been saved to location.txt</p>
</body>
</html>
