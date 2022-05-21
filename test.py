import pandas as pd
import json


def main():

    URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"

    def datagrab():
        df = pd.read_csv(URL)
        df_json = json.loads(df.to_json())
        try:
            # print(df_json["{"]["0"])
            # print(type(df_json))

            if "Note:" or "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency." in df_json["{"]["0"]:
                print("MAX CALLS!!!!")

        except KeyError:
            print(df)
            print("\n")

    datagrab()


if __name__ == "__main__":

    for i in range(20):
        print(i)
        main()
