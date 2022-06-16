"""

This is a file for misc operations that isn't a part of any larger main programme. 


"""

import pandas as pd
import os
import datetime
from dateutil.relativedelta import relativedelta
import math
import array


def start_format_data():

    INDEX_FOLDER = "./index_data/"
    DATA_FOLDER = "./downloaded_data/"
    EARLIEST_INDEX_DATE = "1971-02-05"

    test_data = "AAPL.csv"

    format_data(test_data, INDEX_FOLDER, DATA_FOLDER, EARLIEST_INDEX_DATE)


def format_data(file_name, INDEX_FOLDER, DATA_FOLDER, EARLIEST_INDEX_DATE):
    """

    THE FORMAT OF THE DATA: 

    100 days if actual data

    10 years of index close data.

    NASDAQ (IXIC) from: 1971-02-05
    Dow Jones (DJI) from:  1970-01-02
    S&P (INX) from: 1970-01-02


    Calc spans:

    The oldest index span must start at 1971-02-05 because IXIC





    """

    def calc_spans(dates):

        # check if first date is before limit, set by index + 10y
        valid_dates = []
        for date in dates:

            date_formated = datetime.datetime.strptime(
                str(date.split(" ")[0]), "%Y-%m-%d")

            index_date = datetime.datetime.strptime(
                EARLIEST_INDEX_DATE, "%Y-%m-%d")

            if date_formated < datetime.datetime(index_date.year + 10, index_date.month, index_date.day):
                print("Date before index, skipping: ", date_formated)
                continue

            valid_dates.append(date)

        amount_of_splits = int(round(len(valid_dates) / 100, 1))

        print(amount_of_splits)

        if amount_of_splits < 1:
            print("THIS STOCK HAS LESS THAN 100 DATAPOINTS")
            return

        spans = []
        for split in range(amount_of_splits):

            BATCH_SIZE_OF_ACTUAL_STOCK = 100

            span_index = [(BATCH_SIZE_OF_ACTUAL_STOCK * split),
                          (BATCH_SIZE_OF_ACTUAL_STOCK * split + BATCH_SIZE_OF_ACTUAL_STOCK)]
            span_inner = []
            for i in span_index:
                span_inner.append(valid_dates[i].split(" ")[0])
            spans.append(span_inner)

        # for i, value in enumerate(span):
        #     print(f"INDEX: {i}, SPAN: {value}")

        return spans

    def get_index_values(spans):

        # load index data:
        data_obj = [
            pd.read_csv(INDEX_FOLDER + "DJI_close.csv"),  # 0 = DJI
            pd.read_csv(INDEX_FOLDER + "INX_close.csv"),  # 1 = INX
            pd.read_csv(INDEX_FOLDER + "IXIC_close.csv")  # 2 = IXIC
        ]

        # DJI_df = pd.read_csv(INDEX_FOLDER + "DJI_close.csv")
        # INX_df = pd.read_csv(INDEX_FOLDER + "INX_close.csv")
        # IXIC_df = pd.read_csv(INDEX_FOLDER + "IXIC_close.csv")

        def check_if_date_is_valid(date):

            # Check if index start is a valid date, make sure its not during weekend or something alike
            df = pd.read_csv(INDEX_FOLDER + "DJI_close.csv")

            df["Date"] = df["Date"].str.replace(" 16.00.00", "")
            index_for_date = df.index[df["Date"] ==
                                      date.strftime("%Y-%m-%d")]

            if len(index_for_date.values):
                #print("Returning valid date: ", date.strftime("%Y-%m-%d"))
                return date

            #print("Date not valid, rechecking...")
            return check_if_date_is_valid(date + relativedelta(days=1))

        index_spans = []
        for index, span in enumerate(spans):

            span_start_date = datetime.datetime.strptime(span[0], "%Y-%m-%d")

            index_start_date = span_start_date + relativedelta(years=-10)

            index_start_date = check_if_date_is_valid(index_start_date)

            #print(f"INDEX: {index}, SPAN: {index_start_date}")

            index_spans.append([
                index_start_date.strftime("%Y-%m-%d"),
                span_start_date.strftime("%Y-%m-%d")
            ])

        # Mapping data to spans
        for span in index_spans:
            for index, df in enumerate(data_obj):
                #print("KEY: ", key)
                #print("VALUE: ", value)

                df["Date"] = df["Date"].str.replace(" 16.00.00", "")

                start_index = df.index[df["Date"] == span[0]]
                end_index = df.index[df["Date"] == span[1]]

                if not len(start_index.values):
                    print(f"Start date wrong: {span[0]}")

                if not len(end_index.values):
                    print(f"End date wrong: {span[1]}")

                print(start_index, end_index)
                print("START_VALUES: ",
                      df.at[start_index.values[0], "Date"], "||",  span[0])
                print("END_VALUES: ",
                      df.at[end_index.values[0], "Date"], "||",  span[1])
                print("\n")

        return index_spans

    df = pd.read_csv(DATA_FOLDER + file_name)

    spans = calc_spans(df["Date"])

    get_index_values(spans)


def start_compare_indexes():

    INDEX_FOLDER = "./index_data/"

    first_index = 1
    second_index = 2

    return compare_indexes(INDEX_FOLDER, [first_index, second_index])


def compare_indexes(INDEX_FOLDER, index_array):

    first_index = index_array[0]
    second_index = index_array[1]

    file_names = os.listdir(INDEX_FOLDER)

    indexes = []
    for file in file_names:
        indexes.append(
            pd.read_csv(INDEX_FOLDER + file)
        )

    date_list = []
    for i in indexes:
        date_list.append(i["Date"].to_list())

    no_match = []
    date_len = len(date_list[0])
    for index, dates_1 in enumerate(date_list[first_index]):
        print(f"{index}/{date_len}")
        match = False
        for dates_2 in date_list[second_index]:
            if dates_1 == dates_2:
                match = True
                continue
        if not match:
            no_match.append(dates_1)

    for i in no_match:
        print(i)

    return(no_match, [file_names[first_index], file_names[second_index]])

    #print("COMPARISON: ", no_match)


def start_replace_missing_indexes():

    index_comparison = start_compare_indexes()

    no_match, file_array = index_comparison

    replace_missing_indexes(no_match, file_array)


def replace_missing_indexes(no_match, file_array):

    INPUT_FILE = "./index_data/"

    first_file = file_array[0]
    second_file = file_array[1]

    data1 = pd.read_csv(INPUT_FILE + first_file)
    data2 = pd.read_csv(INPUT_FILE + second_file)

    # check what data is missing values and then add missin value with calculated value
    def check_location_of_missin_data(missing_data):

        if missing_data not in data1["Date"].to_list():
            return "data1"
        if missing_data not in data2["Date"].to_list():
            return "data2"
        print("NO MATCH FOUND!")

    missing_data_loc_arr = []
    for missing_data in no_match:
        missing_data_loc_arr.append(
            check_location_of_missin_data(missing_data))

    print(no_match)
    print(missing_data_loc_arr)

    print("NO_MATCH: ", len(no_match),
          " MISSING_DATA_LOCATION: ", len(missing_data_loc_arr))

    print("file1: ", first_file, "file2: ", second_file)

    def grab_index(df, date):

        days_offset_arr = [1, -1]

        for days_offset in days_offset_arr:

            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H.%M.%S")

            new_date = date_obj + relativedelta(days_offset)

            new_date_string = new_date.strftime("%Y-%m-%d %H.%M.%S")

            print("new_date_string: ", new_date_string)
            print("old_date_string: ", date)

            index = df.index[df["Date"] == new_date_string]

            print("INDEX_LEN: ", len(index.values))

            if len(index.values):
                return index.values[0]

    for index_for_date, date in enumerate(no_match):
        file_name = missing_data_loc_arr[index_for_date]

        if file_name == "data2":
            grab_index_result = grab_index(data1, date)
        elif file_name == "data1":
            grab_index_result = grab_index(data2, date)

        #print("grab_index_result: ", grab_index_result)


if __name__ == "__main__":

    # start_format_data()
    start_compare_indexes()
    # start_replace_missing_indexes()
