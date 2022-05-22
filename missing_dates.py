from datetime import date, timedelta, datetime
import pandas as pd


def main():

    df = pd.read_csv("./test.csv")

    df = df.set_index("timestamp")  # set index to time

    df.index = pd.to_datetime(df.index)  # make the index to actual datetimes

    # start is the index of the last item
    start = df.iloc[len(df.index) - 1].name
    end = df.iloc[0].name  # end is the index of the firs item

    # missing dates is the diffrence between a full list of dates and the list provided by the dataframe
    missing_dates = pd.date_range(start=start, end=end).difference(df.index)

    print("Missing dates:", missing_dates)

    print(type(missing_dates.to_list()))

    missing_dates_list = missing_dates.to_list()

    missing_date_not_weekend = []
    for date in missing_dates_list:
        if date.weekday() > 4:
            continue
        missing_date_not_weekend.append(date)

    print("NOT WEEKEND: ", missing_date_not_weekend)


if __name__ == "__main__":
    main()
