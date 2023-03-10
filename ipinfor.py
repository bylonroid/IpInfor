import json
import socket
import urllib.request

# Get IP address from user input
ip_address = input("Enter an IP address: ")

# Get host name
try:
    host_name = socket.gethostbyaddr(ip_address)[0]
except socket.herror:
    host_name = "Unknown"

# Get geolocation information
url = f"https://ipinfo.io/{ip_address}/json"
response = urllib.request.urlopen(url)
data = json.load(response)

city = data.get("city", "Unknown")
region = data.get("region", "Unknown")
country = data.get("country", "Unknown")
postal = data.get("postal", "Unknown")
latitude, longitude = data.get("loc", "Unknown").split(",")
timezone = data.get("timezone", "Unknown")
org = data.get("org", "Unknown")
asn = data.get("asn", "Unknown")
carrier = data.get("carrier", "Unknown")
mobile = data.get("mobile", "Unknown")
proxy = data.get("proxy", "Unknown")
hosting = data.get("hosting", "Unknown")

# Get Google Maps link
google_maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

# Print information
print(f"IP Address: {ip_address}")
print(f"Host Name: {host_name}")
print(f"City: {city}")
print(f"Region: {region}")
print(f"Country: {country}")
print(f"Postal Code: {postal}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print(f"Timezone: {timezone}")
print(f"Organization: {org}")
print(f"ASN: {asn}")
print(f"Carrier: {carrier}")
print(f"Mobile: {mobile}")
print(f"Proxy: {proxy}")
print(f"Hosting: {hosting}")
print(f"Address: {data['ip']}")
print(f"Google Maps Link: {google_maps_link}")
