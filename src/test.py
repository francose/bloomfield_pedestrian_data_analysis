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
        #remove )
        rng = first[:-1] + rng
        return rng



def main():
    column_names = get_column_names()
    print(column_names)


if __name__ == '__main__':
    main()
