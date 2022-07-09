import phonenumbers
from myphone import number
import opencage
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeoCode

key = "ea296df309fb466fb5473418da3c7c03"

geocoder = OpenCageGeoCode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoomstart=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")