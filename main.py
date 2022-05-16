import pandas as pd

from dataGrab import grab_data_func
from reshapeData import reshape_data_func
from misc import calc_dates_func


def main():
    """

   1. grab data with grab func.

   2. format the data with reshape func

   3. train with the data


    """

    dates = calc_dates_func()

    URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"

    # grab data
    raw_data_arr = []  # array to store all data from diffrent time spans

    for time_interval in dates:
        # grab data and append to arr
        raw_data_arr.append(grab_data_func(
            time_interval[0], time_interval[1], URL))

    # format data
    data_arr = []  # array to store all formatted data

    for raw_data in raw_data_arr:
        # format data and append to arr
        data_arr.append(reshape_data_func(raw_data))

    df = pd.concat(data_arr)  # combine all data to a single dataframe
    # reset the index of the dataframe and update dataframe
    df.reset_index(drop=True, inplace=True)

    print(df)

    df.to_csv("out.csv")


if __name__ == "__main__":
    main()
