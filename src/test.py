'''
Contributors : Sadik Erisen, Arnav Lohe
date : April/6th/2018
Purpose : it is a temporarly test file to mock the data set.
'''

#core modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#gloabls
raw_data = '../data/CrashData.csv'


def read_data():
    test_read  = pd.read_csv(raw_data)
    print(test_read)


def main():
    read = read_data()

if __name__ == '__main__':
    main()
