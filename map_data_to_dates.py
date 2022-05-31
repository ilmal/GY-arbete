from matplotlib.cbook import flatten
from matplotlib.pyplot import step
import pandas as pd
import datetime
import gc
import os

from calc_total_days import calc_days


def main():

    def step_index_def():
        if len(os.listdir("./data_points/final_steps/")) == 0:
            return 0
        index_arr = []
        for file in os.listdir("./data_points/final_steps/"):
            index = int(file.replace("final_", "").replace(".csv", ""))
            index_arr.append(index)

        return max(index_arr) + 1

    global step_index
    step_index = step_index_def()

    # get dates and push into a dataframe
    dates = calc_days()

    print("getting dates")

    column_arr = []
    for date in dates:
        columns = ["open", "high", "low", "close", "volume"]
        for column in columns:
            column_arr.append(date + "_" + column)

    df = pd.DataFrame(columns=column_arr)

    print(f"getting all data from download")
    # get data from downloaded cache
    data_points = os.listdir("./data_points/daily_data/")
    # data_points = ["TSLA", "AAPL", "AAA"]
    print(f"data_points: {len(data_points)}")
    for index, data in enumerate(data_points):
        if " " in data:
            data_points[index] = data.replace(" ", "")
        if ".csv" in data:
            data_points[index] = data
            continue
        data_points[index] = data + ".csv"

    print("reading all data and passing it into data_arr")
    data_list = []
    for data in data_points:
        data_list.append(pd.read_csv(f"./data_points/daily_data/{data}"))
    print("done")

    def create_data_step(data_arr):
        global step_index
        print(f"creating final_step: {step_index}")
        df = pd.concat(data_arr)

        df.reset_index(inplace=True, drop=True)

        df.to_csv(f"./data_points/final_steps/final_{step_index}.csv")
        step_index += 1

        print("done")

    # flatten the data to fit dataframe
    flatten_data = []

    for index, df_old in enumerate(data_list):

        if step_index * 100 >= index:
            print(
                f"skipping for indexes: {index * 100} with index: {step_index}")
            continue

        print("index: ", index, " step_index",
              step_index, "data_len", len(flatten_data))

        missing_value = False
        for column in ["timestamp", "open", "high", "low", "close", "volume"]:
            if column not in df_old.columns.values.tolist():
                missing_value = True
        if missing_value:
            print("incomplete data: ", index)
            continue

        df_old = df_old.set_index("timestamp")

        df_old.to_csv("out.csv")

        df = df_old[["open", "high", "low", "close", "volume"]
                    ].stack().to_frame()  # stacking all data verticaly

        # name each index to have different indexes (eg, "open_0", "open_1", "open_2")
        df.index = [f"{k}_{n}" for n, k in df.index]

        # swap the axis to make the df column based instead of stacked
        df = df.swapaxes(0, 1, copy=True)

        flatten_data.append(df)

        if len(flatten_data) >= 100:
            create_data_step(flatten_data)
            flatten_data = []

    # df = pd.concat(flatten_data)

    # df.reset_index(inplace=True, drop=True)

    # df.to_csv("final.csv")


if __name__ == "__main__":
    main()
