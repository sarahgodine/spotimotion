import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
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
        # print(i + ' '+ str(j))
        if i is 'global':
            global_mean = j

    with open('tracks/global.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        global_data = [float(row[1]) for row in reader]
    with open('tracks/peru.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        peru_data = [float(row[1]) for row in reader]
    with open('tracks/taiwan.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        taiwan_data = [float(row[1]) for row in reader]

    data_list = []
    for country_csv in glob('tracks/*.csv'):
        with open(country_csv, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [float(row[1]) for row in reader]
            # print(data)
        country = country_csv.split('/')[1].split('.')[0]
        # Calculate the T-test on TWO RELATED samples of scores, a and b.
        global_mean = 0.5
        tstat, pvalue = stats.ttest_1samp(data, global_mean)
        data.sort()
        # plt.plot(data, label=country)


        ts = ceil(tstat * 10000.0) / 10000.0
        pv = ceil(pvalue * 100000.0) / 100000.0
        # print(country, np.mean(data), np.std(data), global_mean)
        # print(country, ts, pv)

        data_list.append([country, tstat, pvalue])
        total_data = [data, global_data]

        plt.boxplot(total_data)
        plt.xticks([1,2],(country, 'global'))
        plt.title(country)
        plt.ylabel('valence')
        plt.savefig('plots/'+country+'.png')
        plt.show()
    # plt.ylabel('Valence')
    # plt.legend(ncol=6)
    # plt.xlabel('Song')
    # plt.title('All Countries')
    # plt.savefig('plots/all.png')
    # plt.show()
    # extreme_data = [peru_data, taiwan_data]
    # plt.boxplot(extreme_data)
    # plt.xticks([1,2],('Peru', 'Taiwan'))
    # plt.title('Peru vs. Taiwan')
    # plt.ylabel('valence')
    # plt.savefig('plots/peruvstaiwan.png')
    # plt.show()
    # taiwan_data.sort()
    # peru_data.sort()
    # global_data.sort()
    # plt.plot(taiwan_data, label='Taiwan')
    # plt.plot(peru_data, label='Peru')
    # plt.plot(global_data, label='Global')
    # plt.ylabel('Valence')
    # plt.xlabel('Song')
    # plt.legend()
    # plt.title('Peru and Taiwan vs Global')
    # plt.savefig('plots/big3.png')
    # plt.show()



if __name__ == "__main__":
    main()
