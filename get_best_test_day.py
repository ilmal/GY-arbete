import os
import pandas as pd
import math


def create_column_obj():

    def create_obj(columns):
        result_obj = {}
        for column in columns:
            result_obj[column] = 0
        return result_obj

    # format result obj
    df = pd.read_csv(PATH_TO_FINAL_DATA + os.listdir(PATH_TO_FINAL_DATA)[0])

    # this logic ensures that any "unnamed" columns will be removed from the column_names variable
    unnamed_counter = 0
    for i in range(10):
        if "Unnamed" in str(df.columns[i]):
            unnamed_counter += 1

    column_names = df.columns[unnamed_counter:
                              (NUMBER_OF_COLUMNS_SEARCHED + unnamed_counter) * 5]

    column_list = []
    for column in column_names.to_list():
        if "close" in column:
            column_list.append(column)

    return create_obj(column_list)


def get_data(column_list):

    total_number_of_files = len(os.listdir(PATH_TO_FINAL_DATA))
    for index, file in enumerate(os.listdir(PATH_TO_FINAL_DATA)):

        # print status of calculations
        print(f"Calculating file: {index + 1}/{total_number_of_files}")

        # loop through all days in column_list obj, then get all values of that day from database, if a NaN value is found. Increment column_list obj
        # this will return a column list where the lowest value day has the fewest flaws
        df = pd.read_csv(PATH_TO_FINAL_DATA + file)
        for key in column_list.keys():
            for value in df[key].to_list():
                if math.isnan(value):
                    column_list[key] += 1
        print("Done")

    print(column_list)


def main():

    global NUMBER_OF_COLUMNS_SEARCHED
    global PATH_TO_FINAL_DATA
    global RESULT_OBJ

    NUMBER_OF_COLUMNS_SEARCHED = 20
    PATH_TO_FINAL_DATA = "./data_points/final_steps/"
    RESULT_OBJ = {}

    column_list = create_column_obj()

    # scan entire data_base and append not empty days to column_list

    get_data(column_list)

    # print(column_list)

    """
    
    RESULT FROM PREV SCAN:

    {
        "close_2022-05-20":503,
        "close_2022-05-19":497,
        "close_2022-05-18":498,
        "close_2022-05-17":502,
        "close_2022-05-16":508,
        "close_2022-05-13":507,
        "close_2022-05-12":508,
        "close_2022-05-11":511,
        "close_2022-05-10":510,
        "close_2022-05-09":513,
        "close_2022-05-06":513,
        "close_2022-05-05":514,
        "close_2022-05-04":517,
        "close_2022-05-03":523,
        "close_2022-05-02":523,
        "close_2022-04-29":531,
        "close_2022-04-28":534,
        "close_2022-04-27":537,
        "close_2022-04-26":545,
        "close_2022-04-25":548,
        "close_2022-04-22":556
    }
    
    "close_2022-05-19" is lowest
    
    """


if __name__ == "__main__":
    main()
