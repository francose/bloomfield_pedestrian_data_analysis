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

def read_data(path):
    data = []
    df = pd.read_csv(path, keep_default_na=False,na_values=['NaN'])
    new_dataframe = df['CRASH_LOCATION'] + df['CROSS_STREET_NAME']
    data.append(new_dataframe)
    print(data)

read_data(Path)
