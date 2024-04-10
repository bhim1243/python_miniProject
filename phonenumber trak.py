import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Define the phone number or import it from elsewhere
number = "+977 9848327976"  # Example phone number
# Parse the phone number
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print("Location:", number_location)

# Get service provider information
service_provider = carrier.name_for_number(check_number, "en")
print("Service Provider:", service_provider)

# Geocode the location using OpenCage Geocoding API
key = "c8f80e85addf4de38acfc2433384edb5"  # Replace with your OpenCage API key
geocoder = OpenCageGeocode(key)
query = str(number_location)
results = geocoder.geocode(query)

# Check if results are empty
if results and len(results):
    # Get the first result (most relevant)
    result = results[0]
    lat = result['geometry']['lat']
    lng = result['geometry']['lng']
    print("Location Latitude:", lat)
    print("Location Longitude:", lng)

    # Get current location using OpenCage Geocoding API
    current_location = geocoder.geocode("current location")
    if current_location:
        current_lat = current_location[0]['geometry']['lat']
        current_lng = current_location[0]['geometry']['lng']
        print("Current Location Latitude:", current_lat)
        print("Current Location Longitude:", current_lng)

        # Create and save the map
        map_location = folium.Map(location=[current_lat, current_lng], zoom_start=9)
        folium.Marker([current_lat, current_lng], popup="Current Location").add_to(map_location)
        folium.Marker([lat, lng], popup=number_location).add_to(map_location)
        map_location.save("mylocation.html")  # Save the map as an HTML file
    else:
        print("Unable to get current location.")
else:
    print("No results found for the given location query. Please try again with a different location.")
