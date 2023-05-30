document.getElementById("allowButton").addEventListener("click", getLocationPermission);

function getLocationPermission() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(saveLocation, handleLocationError);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function saveLocation(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  
  // Redirect to another webpage
  window.location.href = "anotherpage.php?lat=" + latitude + "&lng=" + longitude;
}

function handleLocationError(error) {
  console.log(error.message);
  alert("Error occurred while retrieving location.");
}
