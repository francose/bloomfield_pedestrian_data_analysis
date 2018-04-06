'''
Contributors : Sadik Erisen, Arnav Lohe
date : April/6th/2018
Purpose : it is a temporarly test file to mock the data set.
'''

#core modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#supporting modules
import csv, json



#gloabls
raw_data = '../data/CrashData.csv'

#preprocessing
def get_column_names(num=[]):
    with open(raw_data, 'r') as datas:
        reader = csv.reader(datas)
        for i, row in enumerate(reader):
            if (i == 0):
                first = ''.join(row).split()
                lenght_first = len(first)
                # print(first, lenght_firt)
            num.append(len(''.join(row).split()))
        m = max(num)
        rng = range(1, m - lenght_first + 2)
        return rng


def processing__(n=30):
    column_names = get_column_names()
    #post processing
    df = pd.read_csv(raw_data, sep="\s+", names=get_column_names(), index_col=[0], skiprows=1)
    df1 = pd.read_csv(raw_data, sep='\s+', names=range(n))
    #removes all NaN values
    df1 = df1.dropna(axis=1, how='all')
    df1.columns = df1.loc[0].dropna()[:1].append(pd.Series(range(1, len(df1.columns) - len(df1.loc[0].dropna()[:-1]) + 1 )))
    df1 = df1.ix[1:]

    print(df1.head())



def main():
    process = processing__()

if __name__ == '__main__':
    main()
