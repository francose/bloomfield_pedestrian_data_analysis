'''
Author : Sadik Erisen

'''


# core modules
import pandas as pd
import numpy as np
from pandas.compat import StringIO

# supporting modules
import csv
import json

temp=u"""a,b
None,NaN
a,8"""



Path = "../data/paramusdata.csv"


def main():
    data = []
    df = pd.read_csv(Path, keep_default_na=False,na_values=['NaN'])
    new_dataframe = df['CRASH_LOCATION'] + df['CROSS_STREET_NAME']
    for i in new_dataframe:
        data.append(new_dataframe)
    file = open('../data/locations.json', 'w')
    file.write(str(data))

if __name__ == '__main__':
    main()
