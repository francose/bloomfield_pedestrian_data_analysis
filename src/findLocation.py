'''
Author : Sadik Erisen

'''

# core modules
import pandas as pd
import numpy as np
from pandas.compat import StringIO
# supporting modules
import csv, json, requests,time

READ_DATA_PATH = "../data/paramusdata.csv"
POST_URL = "http://maps.google.com/maps/api/geocode/json?address="

#1
def extractColumn():
    df = pd.read_csv(READ_DATA_PATH, keep_default_na=False,na_values=['NaN'])
    pd.options.display.max_rows = 999
    CRASH_LOCATION = df.CRASH_LOCATION
    return CRASH_LOCATION

#2
def URL_POSTFIX():
    data = {}
    data['URL'] = []
    locations = extractColumn()
    for i in locations:
        post_fix_url = POST_URL+ i + ", paramus"
        data['URL'].append({
        'paramus':post_fix_url
        })
    return data['URL']

#4
def createFile( path,data):
    with open(path, 'w') as file:
        json.dump(data ,file)
        file.close

#3
def Location_Result():
    data = []
    urls = URL_POSTFIX()
    for i in urls:
        url = i['paramus']
        try:
            request = requests.post(url)
            if request.status_code == 200:
                time.sleep(.90)
                json_data = request.json()
                for item in json_data['results']:
                    data.append(item)
                    createFile('./static/locations.json',data)
        except ValueError:
            print requests.raise_for_status()
    return request


#4
def getCoordinates(path='./static/locations.json'):
    dataFrame = []
    jsonData = open(path,'r')
    locations_list = json.load(jsonData)
    for main in locations_list:
        main_iterator = main["geometry"]
        location_iter = main_iterator["location"]
        address_components = main["address_components"]
        # long_name = address_components["long_name"]
        # print(long_name)
        lat_iter = location_iter["lat"]
        lng_iter = location_iter["lng"]
        dataFrame.append({'A':"A", 'lat': lat_iter,'lng':lng_iter})
    return dataFrame

def main():
    results = getCoordinates()
    file = createFile('./static/Coordinates.json', results)
    print results
    # Location_Result()



if __name__ == '__main__':
    main()
