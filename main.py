import pandas as pd
import os


def read_data():

    data_arr = []
    # loop through all files in data_points dir and append to array
    for file in os.listdir("./data_points/daily_data/"):
        data_arr.append(pd.read_csv(f"./data_points/daily_data/{file}"))

    return data_arr


def main():

    data_arr = read_data()

    data_sort = []
    for data in data_arr:
        if len(data.index) > 100:
            data_sort.append(data)

    for data in data_sort:
        print(data.head(5))

    # print(data_length[int(len(data_length)/2)])


if __name__ == "__main__":
    main()
