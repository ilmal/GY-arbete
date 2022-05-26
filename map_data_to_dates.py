import pandas as pd
import datetime

from calc_total_days import calc_days


# def format_downloaded_data(data):


def main():
    # get dates and push into a dataframe
    dates = calc_days()

    column_arr = []
    for date in dates:
        columns = ["open", "high", "low", "close", "volume"]
        for column in columns:
            column_arr.append(date + "_" + column)

    print(len(column_arr))

    df = pd.DataFrame(columns=column_arr)

    df.to_csv("dates_df.csv")

    # get data from downloaded cache
    data_points = []
    for index, data in enumerate(data_points):
        if " " in data:
            data_points[index] = data.replace(" ", "")
        data_points[index] = data + ".csv"

    data_list = []
    for data in data_points:
        data_list.append(pd.read_csv(f"./data_points/daily_data/{data}"))


if __name__ == "__main__":
    main()
