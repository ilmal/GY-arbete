import pandas as df
import os


def get_data(index):
    file = PATH_TO_FINAL_DATA + os.listdir(PATH_TO_FINAL_DATA)[index]
    print(file)
    return df.read_csv(file)


def split_data(data, y_column):

    for column in data.columns[::-1]:
        if y_column[-10:] in column:
            if y_column == column:
                continue
            data = data.drop(columns=[column])
    return ([data.pop(y_column), data])


def calc_y(data):
    y_df, df = data

    print(y_df)
    print(df)


def main():
    """

    1. get data
    2. split data
    3. calc if answer is true or false (if stock is up or down)
    4. write data


    """
    global PATH_TO_FINAL_DATA
    PATH_TO_FINAL_DATA = "./data_points/final_steps/"

    y_column = "close_2022-05-19"

    for i in range(1):
        calc_y(split_data(get_data(i), y_column))


if __name__ == "__main__":
    main()
