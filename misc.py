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


def get_raw_data(data_points, companies):
    """
    Example URL refrence

    URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"

    """
    # THIS IS CODE NIGHTMARE, PLEASE GOD FORGIVE MEE! PYTHON NEEDS SWITCH!
    def get_months():
        data_array = [{  # define an array to store all the datapoints. Add the first datapoint as it will always be needed.
            "year": "1",
            "month": "1"
        }]
        if data_points > 30:  # add datapoints based on how many datapoints are requested from main func
            data_array.append({
                "year": "1",
                "month": "2"
            })
        if data_points > 60:
            data_array.append({
                "year": "1",
                "month": "3"
            })
        if data_points > 900:
            data_array.append({
                "year": "1",
                "month": "4"
            })
        if data_points > 120:
            data_array.append({
                "year": "1",
                "month": "5"
            })
        if data_points > 150:
            data_array.append({
                "year": "1",
                "month": "6"
            })
        if data_points > 180:
            data_array.append({
                "year": "1",
                "month": "7"
            })
        if data_points > 210:
            data_array.append({
                "year": "1",
                "month": "8"
            })
        if data_points > 240:
            data_array.append({
                "year": "1",
                "month": "9"
            })
        if data_points > 270:
            data_array.append({
                "year": "1",
                "month": "10"
            })
        if data_points > 300:
            data_array.append({
                "year": "1",
                "month": "11"
            })
        if data_points > 330:
            data_array.append({
                "year": "1",
                "month": "12"
            })
        if data_points > 360:
            data_array.append({
                "year": "2",
                "month": "1"
            })
        if data_points > 390:
            data_array.append({
                "year": "2",
                "month": "2"
            })
        if data_points > 420:
            data_array.append({
                "year": "2",
                "month": "3"
            })
        if data_points > 450:
            data_array.append({
                "year": "2",
                "month": "4"
            })
        if data_points > 480:
            data_array.append({
                "year": "2",
                "month": "5"
            })
        if data_points > 510:
            data_array.append({
                "year": "2",
                "month": "6"
            })
        if data_points > 540:
            data_array.append({
                "year": "2",
                "month": "7"
            })
        if data_points > 570:
            data_array.append({
                "year": "2",
                "month": "8"
            })
        if data_points > 600:
            data_array.append({
                "year": "2",
                "month": "9"
            })
        if data_points > 630:
            data_array.append({
                "year": "2",
                "month": "10"
            })
        if data_points > 660:
            data_array.append({
                "year": "2",
                "month": "11"
            })
        if data_points > 690:
            data_array.append({
                "year": "2",
                "month": "12"
            })
        return data_array

    def get_data(url_arr):  # download every url in the url_array and return and array of all data
        df_raw_data = []
        for url in url_arr:
            df_raw_data.append(pd.read_csv(url))
        # concat all data into a single df before return
        df_data = pd.concat(df_raw_data)
        return df_data

    url_arr = []
    for data_obj in get_months():
        print(data_obj)
        for company in companies:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={company}&interval=5min&slice=year{data_obj['year']}month{data_obj['month']}&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"
            url_arr.append(url)

    df = get_data(url_arr)  # get the df from functions

    return df


if __name__ == "__main__":  # if run directly this will run
    #print(calc_dates_func(10, "2022-05-09 00:00:00"))
    get_raw_data(40, ["TSLA"])
