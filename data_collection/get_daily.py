from audioop import reverse
import pandas as pd
import time
import os
import requests
import io
import sys


global err_counter
err_counter = 0
global reversed
reversed = False


def read_saved_data():

    data_arr = []
    # loop through all files in data_points dir and append to array
    for file in os.listdir("../data_points/daily_data"):
        data_arr.append(file.replace(".csv", ""))

    return data_arr


def download(URL, proxy_index):

    proxies = [
        "amsterdam.nl.socks.nordhold.net",
        "atlanta.us.socks.nordhold.net",
        "dallas.us.socks.nordhold.net",
        "dublin.ie.socks.nordhold.net",
        "ie.socks.nordhold.net",
        "los-angeles.us.socks.nordhold.net",
        "nl.socks.nordhold.net",
        "se.socks.nordhold.net",
        "stockholm.se.socks.nordhold.net",
        "us.socks.nordhold.net"
    ]

    if reversed:
        proxies = proxies[::-1]

    global err_counter
    if err_counter > 0:
        if err_counter + proxy_index > len(proxies) - 1:
            err_counter = 0
        proxy_index += err_counter

    try:
        with requests.Session() as s:
            # s.keep_alive = False
            s.headers['Connection'] = 'close'
            prox = {
                'https': f'socks5://nordvpn@u1.se:U1oregon@{proxies[proxy_index]}:1080'}
            sym = URL.replace("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=",
                              "").replace("&outputsize=full&apikey=U2QRUXVWDVWTRFHW&datatype=csv", "")
            print("downloading:", sym, " with ", proxies[proxy_index])
            r = s.get(URL, proxies=prox)
            df = pd.read_csv(io.StringIO(r.text))
            s.close()
            return df
    except:
        print("ERR OCCURED WITH REQUEST!")
        pass


def grab_data_logic(URL, proxy_index):  # needs URL and origin
    df = download(URL, proxy_index)

    global err_counter
    try:
        if "Note" in df.to_string():
            print("MAX CALLS, changing proxy")
            return grab_data_logic(URL, proxy_index + 1)
        if "Information" in df.to_string():
            print("MAX DAILY CALLS, changing proxy")
            return grab_data_logic(URL, proxy_index + 1)

        print("RES VALID")
        err_counter = 0
        return df
    except:
        print("########################################################################################")
        print("FAILURE OCCURED!!!")
        print("########################################################################################")

        print("DATAFRAME: ", df)

        err_counter += 1

        re_run_main()


def get_data(sym):
    URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={sym}&outputsize=full&apikey=U2QRUXVWDVWTRFHW&datatype=csv"

    df = grab_data_logic(URL, 0)

    return df


def re_run_main():
    delay = 0

    print(f"Value error, rerun code in: {delay}s")
    time.sleep(delay)

    main()


def main():

    print("REVERSE: ", reversed)

    listings_df = pd.read_csv("./ALPHAVANTAGE_LISTINGS.csv")

    listing_sym = listings_df.pop("symbol").to_list()

    if reversed:
        listing_sym = listing_sym[::-1]

    for sym in listing_sym:
        already_grabbed_data = read_saved_data()
        # check if data already exists
        check = False
        for agd in already_grabbed_data:
            if sym == agd:
                check = True
        if check:
            continue

        df = get_data(sym)

        print(
            f"writing data to {sym}.csv, number: {str(len(already_grabbed_data))}")
        df.to_csv(f"../data_points/daily_data/{sym}.csv")


if __name__ == "__main__":
    if sys.argv[len(sys.argv) - 1] == "True":
        reversed = True
    print("ERR COUNTER:", err_counter)
    main()
