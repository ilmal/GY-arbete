import pandas as pd
import os


def read_saved_data():

    data_arr = []
    # loop through all files in data_points dir and append to array
    for file in os.listdir("../data_points/"):
        data_arr.append(pd.read_csv(f"../data_points/{file}"))

    df = pd.concat(data_arr)  # concat all dataframes into a single df

    return df


def shuffle_data(df):
    return df.sample(frac=1).reset_index(drop=True)


if __name__ == "__main__":
    read_saved_data()
