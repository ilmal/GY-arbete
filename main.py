import pandas as pd

from dataGrab import grab_data_func
from reshapeData import reshape_data_func, split_data_to_days_func
from misc import calc_dates_func, get_raw_data


def get_data_from_company(data_slices, company):
    raw_data = get_raw_data(
        data_slices, company)

    raw_data_arr = split_data_to_days_func(raw_data)

    data_arr = []
    for raw_data in raw_data_arr:
        data_arr.append(reshape_data_func(raw_data))

    df = pd.concat(data_arr)

    return df


def main():
    """

   1. grab data with get_raw_data func.

   2. format the data with reshape func



    """

    companies = ["TSLA", "AAPL", "GOOGL", "MSFT", "AMZN",
                 "JNJ", "NVDA", "FB", "UNH", "BRK.B", "XOM"]

    data_slices = 1

    ###############################

    # CURRENT PROBLEM IS THAT get_data_from_company returns array, and so data array is an array of arrays, which I cannot concat into pandas obj

    ###############################

    data_arr = []
    for company in companies:
        data_arr.append(get_data_from_company(data_slices, company))

    df = pd.concat(data_arr)  # combine all data to a single dataframe

    # reset the index of the dataframe and update dataframe
    df.reset_index(drop=True, inplace=True)

    df.to_csv("out.csv")


if __name__ == "__main__":
    main()
