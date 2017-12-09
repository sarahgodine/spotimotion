# Fall 2017, CSCI 4502/5502: Data Mining 
# Sarah Godine
# Final Project: GDelt Findings

import argparse
import csv
import math
import random
import pandas
import numpy
import matplotlib.pyplot as plt

def calculate( dataFile, ithAttr):
    """
    Input Parameters:
        dataFile: The dataset file.
        ithAttre: The ith attribute for which the various properties must be calculated.

    Default value of 0,infinity,-infinity are assigned to all the variables as required. 
    Objective of the function is to calculate:  N (number of objects), min, max, mean, standard deviation, Q1, median, Q3, IQR
    """

    # read in csv
    data = pandas.read_csv(dataFile)

    numObj, minValue, maxValue, mean, stdev, Q1, median, Q3, IQR = [0,"inf","-inf",0,0,0,0,0,0]
    
    #YOUR TASK: Write code to assign the values to the respective variables.

    #avgtone is 35

    # get the attributes of the csv
    columns = ['GLOBALEVENTID','SQLDATE','MonthYear','Year','FractionDate',
        'Actor1Code','Actor1Name','Actor1CountryCode','Actor1KnownGroupCode',
        'Actor1EthnicCode','Actor1Religion1Code','Actor1Religion2Code','Actor1Type1Code',
        'Actor1Type2Code','Actor1Type3Code','Actor2Code','Actor2Name','Actor2CountryCode',
        'Actor2KnownGroupCode','Actor2EthnicCode','Actor2Religion1Code','Actor2Religion2Code',
        'Actor2Type1Code','Actor2Type2Code','Actor2Type3Code','IsRootEvent','EventCode',
        'EventBaseCode','EventRootCode','QuadClass','GoldsteinScale','NumMentions',
        'NumSources','NumArticles','AvgTone','Actor1Geo_Type','Actor1Geo_Fullname',
        'Actor1Geo_CountryCode','Actor1Geo_ADM1Code','Actor1Geo_Lat','Actor1Geo_Long',
        'Actor1Geo_FeatureID','Actor2Geo_Type','Actor2Geo_Fullname','Actor2Geo_CountryCode',
        'Actor2Geo_ADM1Code','Actor2Geo_Lat','Actor2Geo_Long','Actor2Geo_FeatureID','DATEADDED','SOURCEURL']
    attribute = columns[ithAttr-1]
    df = pandas.DataFrame(data, columns = ['GLOBALEVENTID','SQLDATE','MonthYear','Year','FractionDate',
        'Actor1Code','Actor1Name','Actor1CountryCode','Actor1KnownGroupCode',
        'Actor1EthnicCode','Actor1Religion1Code','Actor1Religion2Code','Actor1Type1Code',
        'Actor1Type2Code','Actor1Type3Code','Actor2Code','Actor2Name','Actor2CountryCode',
        'Actor2KnownGroupCode','Actor2EthnicCode','Actor2Religion1Code','Actor2Religion2Code',
        'Actor2Type1Code','Actor2Type2Code','Actor2Type3Code','IsRootEvent','EventCode',
        'EventBaseCode','EventRootCode','QuadClass','GoldsteinScale','NumMentions',
        'NumSources','NumArticles','AvgTone','Actor1Geo_Type','Actor1Geo_Fullname',
        'Actor1Geo_CountryCode','Actor1Geo_ADM1Code','Actor1Geo_Lat','Actor1Geo_Long',
        'Actor1Geo_FeatureID','Actor2Geo_Type','Actor2Geo_Fullname','Actor2Geo_CountryCode',
        'Actor2Geo_ADM1Code','Actor2Geo_Lat','Actor2Geo_Long','Actor2Geo_FeatureID','DATEADDED','SOURCEURL'])

    # calculate
    numObj = df[attribute].count()
    minValue = df[attribute].min()
    maxValue = df[attribute].max()
    mean = df[attribute].mean()
    stdev = df[attribute].std()
    Q1 = df[attribute].quantile(0.25)
    median = df[attribute].median()
    Q3 = df[attribute].quantile(0.75)
    IQR = df[attribute].quantile(0.75) - df[attribute].quantile(0.25)

    # scatter plot
    # plt.scatter(df['T1'],df['T3'])
    # plt.xlabel("T1")
    # plt.ylabel("T3")
    # plt.show()

    return numObj, minValue, maxValue, mean, stdev, Q1, median, Q3, IQR

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW1')
    parser.add_argument('--i', type=int,
                            help="ith attribute of the dataset (2 <= i <= 57)", 
                            default=5,
                            choices=range(2,57),
                            required=True)
    parser.add_argument("--data", type=str, 
                            help="Location of the dataset file",
                            default="lasVegas.csv", 
                            required=True)
    args = parser.parse_args()

    print ','.join(map(str,calculate(args.data,args.i)))
