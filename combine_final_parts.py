import pandas as pd
import os


def main():
    """

    ################################  THIS MIGHT NOT BE NEEDED, INSTEAD USE SMALLER FILES AS BATCHES ###########################

    get data from final steps

    combine data

    output data to final dir

    """

    # get data
    df_arr = []
    for file in os.listdir("./data_points/final_steps"):
        df = pd.read_csv(f"./data_points/final_steps/{file}")

        df_arr.append(df)

    df = pd.concat(df_arr)


if __name__ == "__main__":
    main()
