import pandas as pd
import os


def main():
    """

    Analyze files. Orgiginaly created to se how much data was missing from googles finance data.


    """

    INPUT_PATH = "./grab_data_from_google/formated_data/"

    file = os.listdir(INPUT_PATH)[0]
    df = pd.read_csv(INPUT_PATH + file)

    print(df.head(10))


if __name__ == "__main__":
    main()
