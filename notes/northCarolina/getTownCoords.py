# Import the required library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("5704 Wanderlust Lane, Durham, NC")
print(location.latitude, location.longitude)
#with open('towns.txt', 'r') as f:
#    towns = [line.strip() for line in f]
#
#for town in towns:
#    location = geolocator.geocode(town + ", NC")
#    print(town + "," + str(location.latitude) + "," + str(location.longitude))
   # print("The latitude of the location is: ", location.latitude)
   # print("The longitude of the location is: ", location.longitude)
