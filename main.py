"""
Find phone number location
"""
import phonenumbers
import opencage
import folium
from myPhone import number

# Exctract country name
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)

# Exctract country location
location = geocoder.description_for_number(pepnumber, 'en')
# print(location)

# Get service Provider
from phonenumbers import carrier

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'en'))

# Get location of Phone nummber in Google map
from opencage.geocoder import OpenCageGeocode

# Get API Key from opencagedata.com/dashboard, create a free account
# copy paste the Key into key variable
key = ''

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

# Render the location on the map
myMap = folium.Map(location=[lat, lng], zoom_start=9)
# Arrange the Map
folium.Marker([lat, lng], popup=location).add_to(myMap)
# Save the map inside the folder
myMap.save('trackedLocation.html')














































































































































































