import pandas as pd

from dataGrab import grab_data_func
from reshapeData import reshape_data_func, split_data_to_days_func
from misc import calc_dates_func, get_raw_data


def main():
    """

   1. grab data with grab func.

   2. format the data with reshape func

   3. train with the data


    """

    data_slices = 25  # this is the amount of months worh of data that will be downloaded, 1 - 25: month1year1 - month12year2

    # get dates from func, takes args: (days worth of intervals), (start date)
    dates = calc_dates_func(100, "2022-05-09 00:00:00")

    URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"

    raw_data = get_raw_data(1, ["TSLA"])

    # raw_data.to_csv("raw_data.csv")

    split_data_to_days_func(raw_data)

    # df = reshape_data_func(raw_data)

    # df.to_csv("out.csv")

    # # grab data
    # raw_data_arr = []  # array to store all data from diffrent time spans

    # for time_interval in dates:
    #     # grab data and append to arr
    #     raw_data_arr.append(grab_data_func(
    #         time_interval[0], time_interval[1], URL))

    # # format data
    # data_arr = []  # array to store all formatted data

    # for raw_data in raw_data_arr:  # send the raw data to the reshape func to be formatted
    #     # format data and append to arr
    #     data_arr.append(reshape_data_func(raw_data))

    # df = pd.concat(data_arr)  # combine all data to a single dataframe
    # # reset the index of the dataframe and update dataframe
    # df.reset_index(drop=True, inplace=True)

    # print(df)
    # df.to_csv("out.csv")
if __name__ == "__main__":
    main()
