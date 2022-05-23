import pandas as pd
import os
from numpy import asarray, save, load


def read_data():

    for file in os.listdir("./"):
        if file == "data_cache.npy":
            return read_data_from_cache()

    data_arr = []
    # loop through all files in data_points dir and append to array
    for file in os.listdir("./data_points/daily_data/"):
        data_arr.append(pd.read_csv(f"./data_points/daily_data/{file}"))

    # save data into a cache file
    numpy_data = asarray(data_arr, dtype=object)

    save("data_cache.npy", numpy_data)

    return data_arr


def read_data_from_cache():
    data = load("data_cache.npy", allow_pickle=True)

    return_data = data.tolist()

    return return_data


def main():

    data_arr = read_data()

    data_sort = []
    for data in data_arr:
        if len(data.index) > 100:
            data_sort.append(data)

    data_format_arr = []
    for data in data_sort:
        df = df[["open", "high", "low", "close", "volume"]
                ].stack().to_frame()  # stacking all data verticaly
        # name each index to have different indexes (eg, "open_0", "open_1", "open_2")
        df.index = [f"{k}_{n}" for n, k in df.index]

        # swap the axis to make the df column based instead of stacked
        df = df.swapaxes(0, 1, copy=True)

    """
    
    https://stackoverflow.com/questions/28097222/pandas-merge-two-dataframes-with-different-columns
    
    """


if __name__ == "__main__":
    main()
