#
# Brian
# Retrieve coordiantes of locations 
#

from geopy.geocoders import OpenCage
import pandas as pd

#
# Create a API KEY in https://opencagedata.com/.
# Query is free up to 2,500 requests/day 
#
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxx'

#
# Retrive coordinate
#
def get_coordinates(location):
    geolocator = OpenCage(API_KEY)
    try:
        result = geolocator.geocode(location)
        if result:
            latitude = result.latitude
            longitude = result.longitude
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

#
# Read list of locations from CSV file
#
df = pd.read_csv('Geo_Data.csv')
locations = df['Location'].tolist()

#
# Retrieve coordinates for each location
#
coordinates = []
for location in locations:
    latitude, longitude = get_coordinates(location)
    coordinates.append((location, latitude, longitude))

#
# Create a DataFrame using pandas
#
df = pd.DataFrame(coordinates, columns=["Location", "Latitude", "Longitude"])

#
# Print the DataFrame
#
print(df)

#
# Save to CSV file
#
df.to_csv('Output.csv', index=False)