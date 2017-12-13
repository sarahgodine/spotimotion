import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import argparse
from math import ceil
import pandas as pd
from glob import glob
from scipy import stats

curFeature = 'valence'

def main():
    global_mean = 0
    mean_list = []
    for country_csv in glob('tracks/*.csv'):
        country = country_csv.split('/')[1].split('.')[0]
        df = pd.read_csv(country_csv, usecols=[curFeature])
        m = df[curFeature].mean()
        m = ceil(m * 1000.0) / 1000.0
        country_tuple = (country, round(m, 4))
        mean_list.append(country_tuple)

    mean_list.sort(key=lambda x: x[1], reverse=True)
    for (i, j) in mean_list:
        print(i + ' '+ str(j))
        if i is 'global':
            global_mean = j

    with open('tracks/global.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        global_data = [float(row[1]) for row in reader]

    data_list = []
    for country_csv in glob('tracks/*.csv'):
        with open(country_csv, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [float(row[1]) for row in reader]
            print(data)
        country = country_csv.split('/')[1].split('.')[0]
        # Calculate the T-test on TWO RELATED samples of scores, a and b.
        tstat, pvalue = stats.ttest_1samp(data, global_mean)
        data_list.append([country, tstat, pvalue])
        total_data = [data, global_data]
        plt.boxplot(total_data)
        plt.xticks([1,2],(country, 'global'))
        plt.title(country)
        plt.ylabel('valence')
        # plt.show()
        plt.savefig('plots/'+country+'.png')


if __name__ == "__main__":
    main()
