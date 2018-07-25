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

def extractColumn():
    df = pd.read_csv(READ_DATA_PATH, keep_default_na=False,na_values=['NaN'])
    CRASH_LOCATION = df.CRASH_LOCATION
    return CRASH_LOCATION

def createFile(data):
    with open('./static/locationsss.json', 'w') as file:
        json.dump(data ,file)

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

def Location_Result():
    urls = URL_POSTFIX()
    for i in urls:
        url = i['paramus']
        try:
            request = requests.post(url)
            print request
        except ValueError:
            print requests.raise_for_status()
    return request

def main():
    results = Location_Result()
    print results

    # storeDta = createFile()

if __name__ == '__main__':
    main()








# for i in new_dataframe:
#     newURL = url+i+", paramus"
#     # print newURL
#     time.sleep(.90)
#     r = requests.post(newURL)
#     json_data = r.json()
#     for x in json_data:
#         s =json_data['results']
#         json.dump(s, file)
