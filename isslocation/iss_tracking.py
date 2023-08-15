#!/usr/bin/python3

import urllib.request
import json
import reverse_geocoder as rg

## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## JSON 2 Python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']

# reverse_geocoder MUST be passed a tuple as the argument!
coords_tuple= (lat, lon)

result = rg.search(coords_tuple, verbose=False)
                                 # verbose=False removes an annoying output that reads
                                 # "Loading formatted geocoded file..."
print(result[name])
print('\nLatitude: ', lat)
print('Longitude: ', lon)

