'''
Author : Sadik Erisen

'''


# core modules
import pandas as pd
import numpy as np
from pandas.compat import StringIO


# supporting modules
import csv, json, requests,time


temp=u"""a,b
None,NaN
a,8"""



Path = "../data/paramusdata.csv"
url = "http://maps.google.com/maps/api/geocode/json?address="

def main():

    df = pd.read_csv(Path, keep_default_na=False,na_values=['NaN'])
    new_dataframe = df['CRASH_LOCATION']
    for i in new_dataframe:
        newURL = url+i+", paramus"
        # print newURL
        time.sleep(.90)
        r = requests.post(newURL).json()
        server_message = requests.codes.ok
        if server_message == 200:
            file = open('locations.json', 'w')
            json.dump(r,file)
        else:
            r.raise_for_status()


if __name__ == '__main__':
    main()
