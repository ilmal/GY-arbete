import pandas as pd

#from dataGrab import grab_data_func
from reshapeData import reshape_data_func, split_data_to_days_func
from misc import get_raw_data


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
                 "JNJ", "NVDA", "FB", "UNH", "XOM"]

    companies = ["TSLA", "AAPL"]

    data_slices = 24  # from 0 - 24

    data_arr = []
    for company in companies:
        data = get_data_from_company(data_slices, company)
        data_arr.append(data)

        data.reset_index(inplace=True, drop=True)

        print(f"writing data to {company}.csv (/data_points/5min_data)")
        data.to_csv(f"../data_points/5min_data{company}.csv")

    df = pd.concat(data_arr)  # combine all data to a single dataframe

    # reset the index of the dataframe and update dataframe
    df.reset_index(drop=True, inplace=True)

    df.to_csv("out.csv")


if __name__ == "__main__":
    main()
