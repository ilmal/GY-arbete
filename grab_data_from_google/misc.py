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

        spans = []
        for split in range(1000):

            BATCH_SIZE_OF_ACTUAL_STOCK = 100

            span_index = [(BATCH_SIZE_OF_ACTUAL_STOCK * split),
                          (BATCH_SIZE_OF_ACTUAL_STOCK * split + BATCH_SIZE_OF_ACTUAL_STOCK)]

            if span_index[1] > len(pd.read_csv(DATA_FOLDER + file_name).values.tolist()):
                #print("\n", "BREAKING!", "\n")
                break

            span_inner = []
            for i in span_index:
                span_inner.append(valid_dates[i].split(" ")[0])

            spans.append(span_index)

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

        def check_indexes(span_start_index, span_end_index):
            # THIS FUNCTION RETURNS: span_start_index, spand_end_index, index_start_index, index_end_index

            df = pd.read_csv(DATA_FOLDER + file_name)

            span_end_date = df["Date"][span_end_index]

            index_df = pd.read_csv(INDEX_FOLDER + "DJI_close.csv")

            def check_date(span_end_date):
                return index_df.index[index_df["Date"] ==
                                      span_end_date]

            index_end_index = check_date(span_end_date)

            if not len(index_end_index):
                print("searching")
                index_end_index = check_date((datetime.datetime.strptime(
                    span_end_date, "%Y-%m-%d") + relativedelta(days=1)).strftime("%Y-%m-%d"))

            index_start_index = index_end_index - 2600

            return span_start_index, span_end_index, index_start_index.values[0], index_end_index.values[0]

        index_spans = []
        for span in spans:

            # span_start_date = datetime.datetime.strptime(span[0], "%Y-%m-%d")

            # span_start_date = check_if_span_start_date_is_valid(
            #     span_start_date)

            # index_start_date = span_start_date + relativedelta(years=-10)

            # index_start_date = check_if_date_is_valid(index_start_date)

            #print(f"INDEX: {index}, SPAN: {index_start_date}")

            # index_spans.append([
            #     index_start_date.strftime("%Y-%m-%d"),
            #     span_start_date.strftime("%Y-%m-%d")
            # ])

            # print("\n")
            # print("SPAN[0]: ", span[0])
            # print("SPAN[1]: ", span[1])
            # print("\n")

            span_start_index, span_end_index, index_start_index, index_end_index = check_indexes(
                span[0], span[1])

            # print("SPAN_LEN: ", len(pd.read_csv(DATA_FOLDER +
            #       file_name).values.tolist()), "SPAN_INDEX: ", span_end_index)
            # print("INDEX_LEN: ", len(pd.read_csv(
            #     INDEX_FOLDER + "DJI_close.csv").values.tolist()), "INDEX_INDEX: ", index_end_index)

            if span_start_index < 0 or index_start_index < 0 or span_end_index > len(pd.read_csv(DATA_FOLDER + file_name).values.tolist()) or index_end_index > len(pd.read_csv(INDEX_FOLDER + "DJI_close.csv").values.tolist()):
                print("SKIPPING!")
                continue

            index_spans.append([
                span_start_index, span_end_index, index_start_index, index_end_index
            ])

        # Mapping data to spans
        data_span = []
        index_span = []
        for span in index_spans:
            for index, df_index in enumerate(data_obj):
                #print("KEY: ", key)
                #print("VALUE: ", value)

                df_index["Date"] = df_index["Date"].str.replace(
                    " 16.00.00", "")

                df_data = pd.read_csv(DATA_FOLDER + file_name)
                df_data["Date"] = df_index["Date"].str.replace(
                    " 16.00.00", "")
                # start_index = df.index[df["Date"] == span[0]]
                # end_index = df.index[df["Date"] == span[1]]

                start_span = span[0]
                end_span = span[1]
                start_index = span[2]
                end_index = span[3]

                # if not len(start_index):
                #     print(f"Start date wrong: {span[0]}")

                # if not len(end_index):
                #     print(f"End date wrong: {span[1]}")

                print(start_span, end_span)
                print(start_index, end_index)

                print("INDEX_VALUES: ",
                      df_index.at[start_index, "Date"], "||",  df_index.at[end_index, "Date"])
                print("DATA_VALUES: ",
                      df_data.at[start_span, "Date"], "||",  df_data.at[end_span, "Date"])
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

    for file in file_names:
        if file not in ["DJI_close.csv", "INX_close.csv", "IXIC_close.csv"]:
            file_names.remove(file)

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

    print("FILE1: ", file_names[first_index],
          "FILE2: ", file_names[second_index])

    return(no_match, [file_names[first_index], file_names[second_index]])


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


def start_compare_arrays():

    GOOGLE_IXIC = ['1972-12-28 00:00:00',
                   '1982-09-06 00:00:00',
                   '1987-04-17 00:00:00',
                   '1986-11-27 00:00:00',
                   '1979-05-28 00:00:00',
                   '1984-01-02 00:00:00',
                   '1984-07-04 00:00:00',
                   '1980-11-04 00:00:00',
                   '2001-09-14 00:00:00',
                   '1981-07-03 00:00:00',
                   '1976-04-16 00:00:00',
                   '1979-09-03 00:00:00',
                   '1978-03-24 00:00:00',
                   '1983-09-05 00:00:00',
                   '1979-01-01 00:00:00',
                   '1974-09-02 00:00:00',
                   '1988-02-15 00:00:00',
                   '2012-10-30 00:00:00',
                   '1971-09-06 00:00:00',
                   '1989-02-20 00:00:00',
                   '1975-09-01 00:00:00',
                   '1974-12-25 00:00:00',
                   '1978-01-02 00:00:00',
                   '1977-05-30 00:00:00',
                   '1988-04-01 00:00:00',
                   '1984-12-25 00:00:00',
                   '1986-09-01 00:00:00',
                   '1981-05-25 00:00:00',
                   '1986-03-28 00:00:00',
                   '1987-05-25 00:00:00',
                   '1976-11-02 00:00:00',
                   '1984-02-20 00:00:00',
                   '1983-12-26 00:00:00',
                   '1985-12-25 00:00:00',
                   '1971-07-05 00:00:00',
                   '1978-07-04 00:00:00',
                   '1973-07-04 00:00:00',
                   '1989-09-04 00:00:00',
                   '1977-11-24 00:00:00',
                   '1978-11-23 00:00:00',
                   '1985-04-05 00:00:00',
                   '1976-02-16 00:00:00',
                   '2001-09-13 00:00:00',
                   '1980-07-04 00:00:00',
                   '1976-01-01 00:00:00',
                   '1988-09-05 00:00:00',
                   '1983-11-24 00:00:00',
                   '1989-07-04 00:00:00',
                   '2001-09-12 00:00:00',
                   '1985-09-02 00:00:00',
                   '1979-04-13 00:00:00',
                   '1974-04-12 00:00:00',
                   '1982-12-24 00:00:00',
                   '1980-04-04 00:00:00',
                   '1976-05-31 00:00:00',
                   '1979-12-25 00:00:00',
                   '1981-02-16 00:00:00',
                   '1983-05-30 00:00:00',
                   '1977-12-26 00:00:00',
                   '1972-11-23 00:00:00',
                   '1981-11-26 00:00:00',
                   '1982-02-15 00:00:00',
                   '1987-07-03 00:00:00',
                   '1988-12-26 00:00:00',
                   '1974-05-27 00:00:00',
                   '1983-02-21 00:00:00',
                   '1985-02-18 00:00:00',
                   '1975-12-25 00:00:00',
                   '1987-09-07 00:00:00',
                   '1973-02-19 00:00:00',
                   '1989-12-25 00:00:00',
                   '1980-12-25 00:00:00',
                   '1987-12-25 00:00:00',
                   '1981-04-17 00:00:00',
                   '1978-02-20 00:00:00',
                   '2007-01-02 00:00:00',
                   '1972-03-31 00:00:00',
                   '1979-02-19 00:00:00',
                   '1978-12-25 00:00:00',
                   '1978-05-29 00:00:00',
                   '1975-01-01 00:00:00',
                   '1988-01-01 00:00:00',
                   '2004-06-11 00:00:00',
                   '1985-07-04 00:00:00',
                   '1973-01-25 00:00:00',
                   '1986-02-17 00:00:00',
                   '1986-07-04 00:00:00',
                   '1975-03-28 00:00:00',
                   '1980-09-01 00:00:00',
                   '1984-09-03 00:00:00',
                   '1986-12-25 00:00:00',
                   '1971-11-25 00:00:00',
                   '1980-11-27 00:00:00',
                   '1972-07-04 00:00:00',
                   '1985-05-27 00:00:00',
                   '1974-07-04 00:00:00',
                   '1976-09-06 00:00:00',
                   '1979-11-22 00:00:00',
                   '1979-07-04 00:00:00',
                   '1987-11-26 00:00:00',
                   '1985-01-01 00:00:00',
                   '1972-02-21 00:00:00',
                   '1977-02-21 00:00:00',
                   '1989-05-29 00:00:00',
                   '1981-12-25 00:00:00',
                   '1975-05-26 00:00:00',
                   '1985-09-27 00:00:00',
                   '1976-12-24 00:00:00',
                   '1973-12-25 00:00:00',
                   '2001-09-11 00:00:00',
                   '1975-02-17 00:00:00',
                   '1972-12-25 00:00:00',
                   '1973-01-01 00:00:00',
                   '1973-04-20 00:00:00',
                   '1973-09-03 00:00:00',
                   '1977-07-14 00:00:00',
                   '1986-05-26 00:00:00',
                   '1972-05-29 00:00:00',
                   '1982-04-09 00:00:00',
                   '1974-01-01 00:00:00',
                   '1983-04-01 00:00:00',
                   '1971-05-31 00:00:00',
                   '1975-11-27 00:00:00',
                   '1977-07-04 00:00:00',
                   '1985-11-28 00:00:00',
                   '1984-05-28 00:00:00',
                   '1988-11-24 00:00:00',
                   '1980-01-01 00:00:00',
                   '1974-02-18 00:00:00',
                   '1976-11-25 00:00:00',
                   '1975-07-04 00:00:00',
                   '1982-11-25 00:00:00',
                   '1971-02-15 00:00:00',
                   '1988-05-30 00:00:00',
                   '1972-11-07 00:00:00',
                   '1973-05-28 00:00:00',
                   '1980-05-26 00:00:00',
                   '1981-09-07 00:00:00',
                   '1987-01-01 00:00:00',
                   '1971-12-24 00:00:00',
                   '1987-02-16 00:00:00',
                   '1989-03-24 00:00:00',
                   '1980-02-18 00:00:00',
                   '2018-12-05 00:00:00',
                   '1981-01-01 00:00:00',
                   '1976-07-05 00:00:00',
                   '1994-04-27 00:00:00',
                   '2012-10-29 00:00:00',
                   '1989-11-23 00:00:00',
                   '1977-04-08 00:00:00',
                   '1978-09-04 00:00:00',
                   '1977-09-05 00:00:00',
                   '1971-04-09 00:00:00',
                   '1972-09-04 00:00:00',
                   '1982-07-05 00:00:00',
                   '1973-11-22 00:00:00',
                   '1982-01-01 00:00:00',
                   '1988-07-04 00:00:00',
                   '1984-11-22 00:00:00',
                   '1984-04-20 00:00:00',
                   '1986-01-01 00:00:00',
                   '1989-01-02 00:00:00',
                   '1983-07-04 00:00:00',
                   '1974-11-28 00:00:00',
                   '1982-05-31 00:00:00']

    YAHOO_IXIC = ['1972-12-28 00:00:00',
                  '1982-09-06 00:00:00',
                  '1987-04-17 00:00:00',
                  '1986-11-27 00:00:00',
                  '1979-05-28 00:00:00',
                  '1984-01-02 00:00:00',
                  '1984-07-04 00:00:00',
                  '1980-11-04 00:00:00',
                  '2001-09-14 00:00:00',
                  '1981-07-03 00:00:00',
                  '1976-04-16 00:00:00',
                  '1979-09-03 00:00:00',
                  '1978-03-24 00:00:00',
                  '1983-09-05 00:00:00',
                  '1979-01-01 00:00:00',
                  '1974-09-02 00:00:00',
                  '1988-02-15 00:00:00',
                  '2012-10-30 00:00:00',
                  '1971-09-06 00:00:00',
                  '1989-02-20 00:00:00',
                  '1973-09-26 00:00:00',
                  '1975-09-01 00:00:00',
                  '1974-12-25 00:00:00',
                  '1978-01-02 00:00:00',
                  '1977-05-30 00:00:00',
                  '1988-04-01 00:00:00',
                  '1984-12-25 00:00:00',
                  '1986-09-01 00:00:00',
                  '1981-05-25 00:00:00',
                  '1975-10-16 00:00:00',
                  '1986-03-28 00:00:00',
                  '1987-05-25 00:00:00',
                  '1976-11-02 00:00:00',
                  '1984-02-20 00:00:00',
                  '1983-12-26 00:00:00',
                  '1985-12-25 00:00:00',
                  '1971-07-05 00:00:00',
                  '1978-07-04 00:00:00',
                  '1973-07-04 00:00:00',
                  '1989-09-04 00:00:00',
                  '1977-11-24 00:00:00',
                  '1978-11-23 00:00:00',
                  '1985-04-05 00:00:00',
                  '1976-02-16 00:00:00',
                  '2001-09-13 00:00:00',
                  '1980-07-04 00:00:00',
                  '1976-01-01 00:00:00',
                  '1988-09-05 00:00:00',
                  '1983-11-24 00:00:00',
                  '1989-07-04 00:00:00',
                  '2001-09-12 00:00:00',
                  '1985-09-02 00:00:00',
                  '1979-04-13 00:00:00',
                  '1974-04-12 00:00:00',
                  '1982-12-24 00:00:00',
                  '1980-04-04 00:00:00',
                  '1976-05-31 00:00:00',
                  '1979-12-25 00:00:00',
                  '1981-02-16 00:00:00',
                  '1983-05-30 00:00:00',
                  '1977-12-26 00:00:00',
                  '1972-11-23 00:00:00',
                  '1981-11-26 00:00:00',
                  '1982-02-15 00:00:00',
                  '1987-07-03 00:00:00',
                  '1988-12-26 00:00:00',
                  '1974-05-27 00:00:00',
                  '1983-02-21 00:00:00',
                  '1985-02-18 00:00:00',
                  '1975-12-25 00:00:00',
                  '1987-09-07 00:00:00',
                  '1973-02-19 00:00:00',
                  '1989-12-25 00:00:00',
                  '1980-12-25 00:00:00',
                  '1987-12-25 00:00:00',
                  '1981-04-17 00:00:00',
                  '1978-02-20 00:00:00',
                  '2007-01-02 00:00:00',
                  '1972-03-31 00:00:00',
                  '1979-02-19 00:00:00',
                  '1978-12-25 00:00:00',
                  '1978-05-29 00:00:00',
                  '1975-01-01 00:00:00',
                  '2004-06-11 00:00:00',
                  '1985-07-04 00:00:00',
                  '1973-01-25 00:00:00',
                  '1986-07-04 00:00:00',
                  '1975-03-28 00:00:00',
                  '1980-09-01 00:00:00',
                  '1984-09-03 00:00:00',
                  '1986-12-25 00:00:00',
                  '1971-11-25 00:00:00',
                  '1980-11-27 00:00:00',
                  '1972-07-04 00:00:00',
                  '1985-05-27 00:00:00',
                  '1974-07-04 00:00:00',
                  '1976-09-06 00:00:00',
                  '1979-11-22 00:00:00',
                  '1979-07-04 00:00:00',
                  '1987-11-26 00:00:00',
                  '1985-01-01 00:00:00',
                  '1972-02-21 00:00:00',
                  '1977-02-21 00:00:00',
                  '1989-05-29 00:00:00',
                  '1981-12-25 00:00:00',
                  '1975-05-26 00:00:00',
                  '1985-09-27 00:00:00',
                  '1976-12-24 00:00:00',
                  '1973-12-25 00:00:00',
                  '2001-09-11 00:00:00',
                  '1975-02-17 00:00:00',
                  '1972-12-25 00:00:00',
                  '1973-01-01 00:00:00',
                  '1973-04-20 00:00:00',
                  '1973-09-03 00:00:00',
                  '1977-07-14 00:00:00',
                  '1986-05-26 00:00:00',
                  '1972-05-29 00:00:00',
                  '1982-04-09 00:00:00',
                  '1974-01-01 00:00:00',
                  '1983-04-01 00:00:00',
                  '1971-05-31 00:00:00',
                  '1975-11-27 00:00:00',
                  '1977-07-04 00:00:00',
                  '1985-11-28 00:00:00',
                  '1984-05-28 00:00:00',
                  '1988-11-24 00:00:00',
                  '1980-01-01 00:00:00',
                  '1974-02-18 00:00:00',
                  '1976-11-25 00:00:00',
                  '1975-07-04 00:00:00',
                  '1982-11-25 00:00:00',
                  '1971-02-15 00:00:00',
                  '1988-05-30 00:00:00',
                  '1972-11-07 00:00:00',
                  '1973-05-28 00:00:00',
                  '1980-05-26 00:00:00',
                  '1974-10-07 00:00:00',
                  '1981-09-07 00:00:00',
                  '1987-01-01 00:00:00',
                  '1971-12-24 00:00:00',
                  '1987-02-16 00:00:00',
                  '1989-03-24 00:00:00',
                  '1980-02-18 00:00:00',
                  '2018-12-05 00:00:00',
                  '1981-01-01 00:00:00',
                  '1976-07-05 00:00:00',
                  '1994-04-27 00:00:00',
                  '2012-10-29 00:00:00',
                  '1989-11-23 00:00:00',
                  '1977-04-08 00:00:00',
                  '1978-09-04 00:00:00',
                  '1977-09-05 00:00:00',
                  '1971-04-09 00:00:00',
                  '1972-09-04 00:00:00',
                  '1982-07-05 00:00:00',
                  '1973-11-22 00:00:00',
                  '1982-01-01 00:00:00',
                  '1988-07-04 00:00:00',
                  '1984-11-22 00:00:00',
                  '1984-04-20 00:00:00',
                  '1986-01-01 00:00:00',
                  '1989-01-02 00:00:00',
                  '1983-07-04 00:00:00',
                  '1974-11-28 00:00:00',
                  '1982-05-31 00:00:00']

    GOOGLE_DJI = ['1977-05-30 00:00:00',
                  '1972-12-28 00:00:00',
                  '1973-04-20 00:00:00',
                  '1977-12-26 00:00:00',
                  '1973-07-04 00:00:00',
                  '1979-02-19 00:00:00',
                  '1982-12-24 00:00:00',
                  '1973-01-01 00:00:00',
                  '1976-01-01 00:00:00',
                  '1974-12-25 00:00:00',
                  '1972-03-31 00:00:00',
                  '1988-12-26 00:00:00',
                  '1986-03-28 00:00:00',
                  '1987-04-17 00:00:00',
                  '1973-09-03 00:00:00',
                  '1980-02-18 00:00:00',
                  '1974-07-04 00:00:00',
                  '1989-12-25 00:00:00',
                  '1982-11-25 00:00:00',
                  '1980-11-27 00:00:00',
                  '1981-11-26 00:00:00',
                  '1987-01-01 00:00:00',
                  '1989-07-04 00:00:00',
                  '1989-02-20 00:00:00',
                  '1988-11-24 00:00:00',
                  '1981-02-16 00:00:00',
                  '1981-05-25 00:00:00',
                  '1971-04-09 00:00:00',
                  '1975-05-26 00:00:00',
                  '1972-11-07 00:00:00',
                  '1988-02-15 00:00:00',
                  '2018-12-05 00:00:00',
                  '1978-09-04 00:00:00',
                  '1985-02-18 00:00:00',
                  '1977-02-21 00:00:00',
                  '1984-02-20 00:00:00',
                  '1973-12-25 00:00:00',
                  '1987-05-25 00:00:00',
                  '1980-04-04 00:00:00',
                  '1971-01-01 00:00:00',
                  '1972-05-29 00:00:00',
                  '1983-12-26 00:00:00',
                  '1989-11-23 00:00:00',
                  '1975-09-01 00:00:00',
                  '1970-03-27 00:00:00',
                  '1984-12-25 00:00:00',
                  '1984-04-20 00:00:00',
                  '1988-09-05 00:00:00',
                  '1985-09-02 00:00:00',
                  '1978-05-29 00:00:00',
                  '1976-11-02 00:00:00',
                  '1976-04-16 00:00:00',
                  '1988-05-30 00:00:00',
                  '1989-03-24 00:00:00',
                  '1978-07-04 00:00:00',
                  '1973-05-28 00:00:00',
                  '1974-11-28 00:00:00',
                  '1979-12-25 00:00:00',
                  '1974-02-18 00:00:00',
                  '1979-07-04 00:00:00',
                  '1976-11-25 00:00:00',
                  '1973-11-22 00:00:00',
                  '1978-02-20 00:00:00',
                  '1980-09-01 00:00:00',
                  '1985-07-04 00:00:00',
                  '1980-07-04 00:00:00',
                  '1977-07-04 00:00:00',
                  '1987-07-03 00:00:00',
                  '1985-01-01 00:00:00',
                  '1971-11-25 00:00:00',
                  '1971-09-06 00:00:00',
                  '1971-02-15 00:00:00',
                  '2007-01-02 00:00:00',
                  '1972-12-25 00:00:00',
                  '1975-01-01 00:00:00',
                  '1979-04-13 00:00:00',
                  '1982-04-09 00:00:00',
                  '1983-02-21 00:00:00',
                  '1974-05-27 00:00:00',
                  '1989-05-29 00:00:00',
                  '1985-11-28 00:00:00',
                  '1977-04-08 00:00:00',
                  '1976-02-16 00:00:00',
                  '1987-11-26 00:00:00',
                  '1978-03-24 00:00:00',
                  '1972-07-04 00:00:00',
                  '1975-03-28 00:00:00',
                  '1986-05-26 00:00:00',
                  '1980-05-26 00:00:00',
                  '1987-09-07 00:00:00',
                  '1970-02-23 00:00:00',
                  '1978-01-02 00:00:00',
                  '1988-04-01 00:00:00',
                  '1981-07-03 00:00:00',
                  '1985-05-27 00:00:00',
                  '1972-02-21 00:00:00',
                  '1986-12-25 00:00:00',
                  '1976-12-24 00:00:00',
                  '2004-06-11 00:00:00',
                  '1975-07-04 00:00:00',
                  '1977-11-24 00:00:00',
                  '1971-07-05 00:00:00',
                  '2012-10-29 00:00:00',
                  '1989-09-04 00:00:00',
                  '1970-09-07 00:00:00',
                  '1985-09-27 00:00:00',
                  '1970-11-26 00:00:00',
                  '1973-02-19 00:00:00',
                  '1973-01-25 00:00:00',
                  '1970-12-25 00:00:00',
                  '1978-11-23 00:00:00',
                  '1975-11-27 00:00:00',
                  '1981-01-01 00:00:00',
                  '1979-01-01 00:00:00',
                  '1984-07-04 00:00:00',
                  '1982-07-05 00:00:00',
                  '1982-01-01 00:00:00',
                  '1975-12-25 00:00:00',
                  '1979-05-28 00:00:00',
                  '1986-07-04 00:00:00',
                  '1987-12-25 00:00:00',
                  '1989-01-02 00:00:00',
                  '1975-02-17 00:00:00',
                  '1972-09-04 00:00:00',
                  '1976-07-05 00:00:00',
                  '1979-09-03 00:00:00',
                  '1983-09-05 00:00:00',
                  '1976-05-31 00:00:00',
                  '1971-05-31 00:00:00',
                  '1978-12-25 00:00:00',
                  '1976-09-06 00:00:00',
                  '1982-02-15 00:00:00',
                  '1974-09-02 00:00:00',
                  '1987-02-16 00:00:00',
                  '1977-07-14 00:00:00',
                  '1982-09-06 00:00:00',
                  '1981-12-25 00:00:00',
                  '1980-01-01 00:00:00',
                  '1984-01-02 00:00:00',
                  '1972-11-23 00:00:00',
                  '1971-12-24 00:00:00',
                  '1981-04-17 00:00:00',
                  '1986-01-01 00:00:00',
                  '1984-05-28 00:00:00',
                  '1979-11-22 00:00:00',
                  '1983-04-01 00:00:00',
                  '1980-12-25 00:00:00',
                  '1974-01-01 00:00:00',
                  '1986-09-01 00:00:00',
                  '1985-12-25 00:00:00',
                  '1988-07-04 00:00:00',
                  '1974-04-12 00:00:00',
                  '1977-09-05 00:00:00',
                  '1970-07-03 00:00:00']

    compare_arrays(GOOGLE_IXIC, GOOGLE_DJI)


def compare_arrays(array1, array2):

    match_list = []
    not_match_list = []

    for i1 in array1:
        match = False
        for i2 in array2:
            if i1 == i2:
                match = True
                match_list.append(i1)
        if not match:
            not_match_list.append(i1)

    print("MATCH: ", match_list)
    print("\n")
    print("NOT_MATCH: ", not_match_list)


if __name__ == "__main__":

    start_format_data()
    # start_compare_indexes()
    # start_replace_missing_indexes()
    # start_compare_arrays()
