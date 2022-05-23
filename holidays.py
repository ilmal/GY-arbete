import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests


def main():

    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022
             ]

    i = 0

    date_arr = []
    for year in years:
        r = requests.get(
            f"http://www.market-holidays.com/{year}"
        )

        soup = BeautifulSoup(r.text, "html.parser")

        for index, e in enumerate(soup.find_all("td")):
            if index % 2:
                e = str(e).replace("<td>", "").replace("</td>", "")
                date_arr.append(datetime.datetime.strptime(e, "%B %d, %Y"))

        # i += 1
        # if i > 0:
        #     break

    for e in date_arr:
        print(e)


if __name__ == "__main__":
    main()
