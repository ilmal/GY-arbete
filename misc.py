from datetime import datetime, timedelta
import pandas as pd


def calc_dates_func(data_points, start_date):

    if start_date == None or data_points == None:  # throw err if no values are passed to the func
        print("ERR: Need values for data_points and start_date")
        return

    # converting start date to a date obj
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")

    span_arr = []  # define return array

    for i in range(data_points):  # loop though all datapoints that was requested

        start_date_value = start_date_obj - \
            timedelta(days=i)  # define the start of the span
        end_date_value = start_date_obj - \
            timedelta(days=i+1)  # define the end of the span

        # add the span to the return list
        span_arr.append([str(start_date_value), str(end_date_value)])

    # return the list containing all the spans requested by: datapoints (number of spans) and start_date (start of the first span)
    return span_arr


def get_raw_data(data_slices, companies):
    """
    Example URL refrence

    URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"

    """

    def get_months(data_slices):

        if data_slices > 25:
            raise Exception("CUSTOM: datapoints > 24 not allowed")

        return_arr = []

        for i in range(data_slices):
            i += 1
            data_obj = {
                "month": "1",
                "year": "1"
            }
            if i > 12:
                data_obj["year"] = str(2)
                data_obj["month"] = str(i - 12)
            else:
                data_obj["month"] = str(i)
            return_arr.append(data_obj)
        return return_arr

    def get_data(url_arr):  # download every url in the url_array and return and array of all data
        df_raw_data = []
        for url in url_arr:
            df_raw_data.append(pd.read_csv(url))
        # concat all data into a single df before return
        df_data = pd.concat(df_raw_data)
        return df_data

    url_arr = []
    for data_obj in get_months(data_slices):
        for company in companies:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={company}&interval=5min&slice=year{data_obj['year']}month{data_obj['month']}&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"
            url_arr.append(url)

    for url in url_arr:
        print(url)

    df = get_data(url_arr)  # get the df from functions

    return df


if __name__ == "__main__":  # if run directly this will run
    # print(calc_dates_func(10, "2022-05-09 00:00:00"))
    get_raw_data(25, ["TSLA"])
