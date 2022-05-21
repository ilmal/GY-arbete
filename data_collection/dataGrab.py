import pandas as pd
import datetime as dt
import numpy as np

pd.set_option("display.max_rows", 5000)


def grab_data_func(LOWER_DATE="2022-05-11 00:00:00",
                   UPPER_DATE="2022-05-12 00:00:00",
                   URL="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"
                   ):

    df = pd.read_csv(URL)

    lower_limit_day = dt.datetime.strptime(LOWER_DATE, "%Y-%m-%d %H:%M:%S")
    upper_limit_day = dt.datetime.strptime(UPPER_DATE, "%Y-%m-%d %H:%M:%S")

    for index, row in df.iterrows():  # dropping all data that doesn't align with my set date above
        # dropping all data before the lower limit
        if lower_limit_day > dt.datetime.strptime(row["time"], '%Y-%m-%d %H:%M:%S'):
            df.drop(index, inplace=True)

        # dropping all data after the upper limit
        if upper_limit_day < dt.datetime.strptime(row["time"], '%Y-%m-%d %H:%M:%S'):
            df.drop(index, inplace=True)

    # flip dataframe
    df = df.loc[::-1].set_index(df.index)

    df.reset_index(inplace=True)
    df.drop(columns="index", inplace=True)

    return df


grab_data_func()
