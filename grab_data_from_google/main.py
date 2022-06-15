import asyncio
import threading
import pandas as pd
import os

from grab_data import grab_data
from move_data import move_data


async def main():

    url_list = [
        "https://docs.google.com/spreadsheets/d/1I2tt5_pZlXiQZKwZKYMgAyM5TzaFoYXuKVWf2R-gkdY/edit#gid=0",  # 0
        "https://docs.google.com/spreadsheets/d/1Juj4Jbq4hsdu84u2Fc77DyAHhDD1jNLJYV3r-q9hU5M/edit#gid=0",  # 1
        "https://docs.google.com/spreadsheets/d/1sarsE1qryAn9xnOMwnHKaW5ymcDMA5fkQ1n8AFi41Yw/edit#gid=0",  # 2
        "https://docs.google.com/spreadsheets/d/1Mzag0MkiJ0VJOYsGyPK20DCUl5kXS4GbgITFQAFyyJw/edit#gid=0",  # 3
        "https://docs.google.com/spreadsheets/d/1FWfjhiZG2MH9PwBqLnk73nNIvsf_cVToCrVwM6S_s1c/edit#gid=0",  # 4
        "https://docs.google.com/spreadsheets/d/1BfqVFF-zTVeX45bHBGhzSss_obv31q_8oSgYQx3nODM/edit#gid=0",  # 5
        "https://docs.google.com/spreadsheets/d/1Lu3Zj3A9d8Lze5shH8b7H_Vk1QFPFeRR4g047CsvSY8/edit#gid=0",  # 6
        "https://docs.google.com/spreadsheets/d/1dm-G469uymBHKGENJiW1ALVOc7IiuMLBHQRhc7QNMRs/edit#gid=0",  # 7
        "https://docs.google.com/spreadsheets/d/1sPmC4oTGqjB7vB2AQevt_9avQl940Ggfhk-evyfDmUc/edit#gid=0",  # 8
        "https://docs.google.com/spreadsheets/d/1JEtD_ylZmxtaLZfbaP10PTfFjw8vricb7XhbsCwRtZE/edit#gid=0",  # 9
        "https://docs.google.com/spreadsheets/d/1XtE4tjxy_K4wBIl4I1Zk-3pR1JkOwTkmbHDKDGeD1Yo/edit#gid=0",  # 10
        "https://docs.google.com/spreadsheets/d/1zWg8xJtvxBF_0P27l4jG3evo6FoOHLnKKZv4JPAcgu4/edit#gid=0"   # 11
    ]

    company_index = pd.read_csv("./nasdaq.csv").iloc[:, 0].to_list()

    def choose_stock(index):

        if len(os.listdir("./downloaded_data/")) == 0:
            return company_index[index]

        for file in os.listdir("./downloaded_data/"):
            # print("INDEX: ", str(company_index[index] + ".csv"))
            # print("FILE: ", str(file))
            if str(company_index[index] + ".csv") == str(file):
                #print("MATCH: ", str(company_index[index] + ".csv"), str(file))
                return choose_stock(index + 12)

        #print("STOCK FOUND AND ACCEPTED")
        return company_index[index]

    def run(index, ):
        stock = choose_stock(index)
        print("STOCK: ", stock)

        print("Running through index: ", index)
        asyncio.run(grab_data(url_list[index], stock))
        move_data(index, stock)
        return True

    t0 = threading.Thread(target=run, args=(0, ))
    t1 = threading.Thread(target=run, args=(1, ))
    t2 = threading.Thread(target=run, args=(2, ))
    t3 = threading.Thread(target=run, args=(3, ))
    t4 = threading.Thread(target=run, args=(4, ))
    t5 = threading.Thread(target=run, args=(5, ))
    t6 = threading.Thread(target=run, args=(6, ))
    t7 = threading.Thread(target=run, args=(7, ))
    t8 = threading.Thread(target=run, args=(8, ))
    t9 = threading.Thread(target=run, args=(9, ))
    t10 = threading.Thread(target=run, args=(10, ))
    t11 = threading.Thread(target=run, args=(11, ))

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()

    return True


async def start_main():

    while True:
        await main()

if __name__ == "__main__":
    asyncio.run(start_main())
