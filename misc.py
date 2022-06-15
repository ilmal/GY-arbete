"""

This file is intended for misc scripts
My directory is currently quite crowded with misc files... That should change


"""

import os
import pandas as df


def delete_bad_data():

    INPUT_LOCATION = "./grab_data_from_google/downloaded_data/"

    def get_empty_files(file_path):
        counter = 0

        return_arr = []
        for file in os.listdir(INPUT_LOCATION):

            file_path = INPUT_LOCATION + file

            file_name = file_path.split("/")[-1].split(".")[0]

            # check if size of file is 0
            if os.stat(file_path).st_size < 100:
                counter += 1
                print(f'File: {file_name} is empty, {counter}')
                return_arr.append(file_path)
        return return_arr

    list = get_empty_files(INPUT_LOCATION)

    for file in list:
        os.remove(file)


if __name__ == "__main__":
    delete_bad_data()
