import phonenumbers
from myphoone import number
import opencage
import folium

from phonenumbers import geocoder

#this part for print number location
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

#this part for print service provider name
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

key = "9a43d3c379b249a79edfeb32dc33d66f"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat , lng], zoom_start = 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)

myMap.save("mylocation.html")
