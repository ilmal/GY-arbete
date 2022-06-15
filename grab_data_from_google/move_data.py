import os
from tabnanny import check
import time


def move_data(index, stock):
    DOWNLOAD_PATH = "/home/main-pc/Downloads"

    files = os.listdir(DOWNLOAD_PATH)

    def check_for_file(files, counter=0):
        print(f"INDEX: {index}", "Scanning for files...")
        for file in files:
            if f'bot_data_{index} - Blad1.csv' in file:
                print("File found")
                return file
        if counter < 10:
            print(
                f"INDEX: {index}", f"File: 'bot_data_{index} - Blad1.csv' not found. Rescanning in 5 seconds")
            time.sleep(5)
            check_for_file(files, counter + 1)
        else:
            print(f"INDEX: {index}", "ERR CHECKING FOR FILE, FILE NOT FOUND")
            return

    file = check_for_file(files)

    os.rename(
        f"{DOWNLOAD_PATH}/{file}", f"/home/main-pc/programing/GY-arbete/grab_data_from_google/downloaded_data/{stock}.csv")
    print("Data transfer complete")
    return
