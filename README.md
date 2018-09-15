# sg-school-data-json
Script written to convert school data from .csv to geocoded .json file.

## Datset 
https://data.gov.sg/dataset/school-directory-and-information

## Original CSV file

| school_name | url_address | address |
| ----------- | :---------: | :-------:|
| NATIONAL JUNIOR COLLEGE | www.nationaljc.moe.edu.sg | 37 HILLCREST ROAD |

## After converting to JSON file
```
[{
"school_name": "NATIONAL JUNIOR COLLEGE", 
"address": "37 HILLCREST ROAD", 
"lat": 38.7880067, 
"lng": -104.8568176
}]
```

## Geocoding
Geocoding is done using the Google Geocoding API - You can get the API key via the Google Cloud Platform.

## External libraries used 
dotenv - To store environment variables - **API Keys should never be exposed in the code!!!!**
requests - For HTTP Request to Google Geocoding API
pandas - To parse csv file

