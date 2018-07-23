'''
Contributors : Sadik Erisen, Arnav Lohe
date : April/6th/2018
Purpose : it is a temporarly test file to mock the data set.
'''

# core modules
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# supporting modules
import csv
import json


# gloabls
raw_data = '../data/CrashData.csv'

#Test correlation for the preprocessing step.
# preprocessing
def preprocessing():
    dataframe = pd.read_csv(raw_data)
    df = pd.DataFrame(dataframe)
    dropped = df.dropna(axis=1, how="any")
    correlation = dropped.corr(method='pearson')
    print(correlation)


def main():

    correlation = preprocessing()








if __name__ == '__main__':
    main()
