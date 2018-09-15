import pandas as pd
import json
import requests
import os

from dotenv import load_dotenv

# Add our .env file to environment
load_dotenv()

def convert_postal_to_lat_lng(school):

    # Google Geocoding API Url
    geo_api = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'. format(school_name, os.getenv('API_KEY'))

    # HTTP GET Request
    r = requests.get(geo_api)

    # Get the JSON response
    json_response = r.json()

    location_coord = json_response['results'][0]['geometry']['location']
    # Return JSON object with returned lat and lng
    return {
        **school,
        'lat': location_coord['lat'],
        'lng': location_coord['lng'],
    }


def convert_list_to_dict(school):
    print('School item: ', school)
    return {
        'school_name': school[0],
        'address': school[1]
    }

# Store the json file in the local directory
def store_json(school_list):
    with open('school.json', 'w') as out:
        json.dump(school_list, out)

# Csv file in local directory
school_csv_file = './general-information-of-schools.csv'

# Read the csv file using pandas
schools_df = pd.read_csv(school_csv_file)

# Get the school name and address and convert to a list
school_list = schools_df[['school_name', 'address']].values.tolist()

# Lambda function to convert the list array to list json
school_dict_list = list(map(convert_list_to_dict, school_list))

# Get the lat and lng for each item in the list
school_with_coord_list = list(map(convert_postal_to_lat_lng, school_dict_list))

# Store the result as .json
store_json(school_with_coord_list)







