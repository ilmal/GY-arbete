import datetime
import pandas as pd


def main():

    start = "1990-01-01 00:00:00"
    end = datetime.date.today()

    all_dates = pd.date_range(start=start, end=end)

    all_dates_arr = []
    for date in all_dates.to_list():
        all_dates_arr.append(str(date))

    not_counted_days = []
    for date in all_dates:
        if date.weekday() > 4:
            continue
        not_counted_days.append(str(date))

    holidays = ["1990-01-01 00:00:00", "1990-01-15 00:00:00", "1990-02-19 00:00:00", "1990-04-13 00:00:00", "1990-05-28 00:00:00", "1990-07-04 00:00:00", "1990-09-03 00:00:00", "1990-11-22 00:00:00", "1990-12-25 00:00:00", "1991-01-01 00:00:00", "1991-01-21 00:00:00", "1991-02-18 00:00:00", "1991-03-29 00:00:00", "1991-05-27 00:00:00", "1991-07-04 00:00:00", "1991-09-02 00:00:00", "1991-11-28 00:00:00", "1991-12-25 00:00:00", "1992-01-01 00:00:00", "1992-01-20 00:00:00", "1992-02-17 00:00:00", "1992-04-17 00:00:00", "1992-05-25 00:00:00", "1992-07-03 00:00:00", "1992-09-07 00:00:00", "1992-11-26 00:00:00", "1992-12-25 00:00:00", "1993-01-01 00:00:00", "1993-01-18 00:00:00", "1993-02-15 00:00:00", "1993-04-09 00:00:00", "1993-05-31 00:00:00", "1993-07-05 00:00:00", "1993-09-06 00:00:00", "1993-11-25 00:00:00", "1993-12-24 00:00:00", "1993-12-31 00:00:00", "1994-01-17 00:00:00", "1994-02-21 00:00:00", "1994-04-01 00:00:00", "1994-05-30 00:00:00", "1994-07-04 00:00:00", "1994-09-05 00:00:00", "1994-11-24 00:00:00", "1994-12-26 00:00:00", "1995-01-02 00:00:00", "1995-01-16 00:00:00", "1995-02-20 00:00:00", "1995-04-14 00:00:00", "1995-05-29 00:00:00", "1995-07-04 00:00:00", "1995-09-04 00:00:00", "1995-11-23 00:00:00", "1995-12-25 00:00:00", "1996-01-01 00:00:00", "1996-01-15 00:00:00", "1996-02-19 00:00:00", "1996-04-05 00:00:00", "1996-05-27 00:00:00", "1996-07-04 00:00:00", "1996-09-02 00:00:00", "1996-11-28 00:00:00", "1996-12-25 00:00:00", "1997-01-01 00:00:00", "1997-01-20 00:00:00", "1997-02-17 00:00:00", "1997-03-28 00:00:00", "1997-05-26 00:00:00", "1997-07-04 00:00:00", "1997-09-01 00:00:00", "1997-11-27 00:00:00", "1997-12-25 00:00:00", "1998-01-01 00:00:00", "1998-01-19 00:00:00", "1998-02-16 00:00:00", "1998-04-10 00:00:00", "1998-05-25 00:00:00", "1998-07-03 00:00:00", "1998-09-07 00:00:00", "1998-11-26 00:00:00", "1998-12-25 00:00:00", "1999-01-01 00:00:00", "1999-01-18 00:00:00", "1999-02-15 00:00:00", "1999-04-02 00:00:00", "1999-05-31 00:00:00", "1999-07-05 00:00:00", "1999-09-06 00:00:00", "1999-11-25 00:00:00", "1999-12-24 00:00:00", "1999-12-31 00:00:00", "2000-01-17 00:00:00", "2000-02-21 00:00:00", "2000-04-21 00:00:00", "2000-05-29 00:00:00", "2000-07-04 00:00:00", "2000-09-04 00:00:00", "2000-11-23 00:00:00", "2000-12-25 00:00:00", "2001-01-01 00:00:00", "2001-01-15 00:00:00", "2001-02-19 00:00:00", "2001-04-13 00:00:00", "2001-05-28 00:00:00", "2001-07-04 00:00:00", "2001-09-03 00:00:00", "2001-11-22 00:00:00", "2001-12-25 00:00:00", "2002-01-01 00:00:00", "2002-01-21 00:00:00", "2002-02-18 00:00:00", "2002-03-29 00:00:00", "2002-05-27 00:00:00", "2002-07-04 00:00:00", "2002-09-02 00:00:00", "2002-11-28 00:00:00", "2002-12-25 00:00:00", "2003-01-01 00:00:00", "2003-01-20 00:00:00", "2003-02-17 00:00:00", "2003-04-18 00:00:00", "2003-05-26 00:00:00", "2003-07-04 00:00:00", "2003-09-01 00:00:00", "2003-11-27 00:00:00", "2003-12-25 00:00:00", "2004-01-01 00:00:00", "2004-01-19 00:00:00", "2004-02-16 00:00:00", "2004-04-09 00:00:00", "2004-05-31 00:00:00", "2004-07-05 00:00:00", "2004-09-06 00:00:00", "2004-11-25 00:00:00", "2004-12-24 00:00:00", "2004-12-31 00:00:00", "2005-01-17 00:00:00", "2005-02-21 00:00:00", "2005-03-25 00:00:00", "2005-05-30 00:00:00", "2005-07-04 00:00:00", "2005-09-05 00:00:00", "2005-11-24 00:00:00", "2005-12-26 00:00:00", "2006-01-02 00:00:00", "2006-01-16 00:00:00", "2006-02-20 00:00:00", "2006-04-14 00:00:00", "2006-05-29 00:00:00", "2006-07-04 00:00:00", "2006-09-04 00:00:00", "2006-11-23 00:00:00", "2006-12-25 00:00:00", "2007-01-01 00:00:00", "2007-01-15 00:00:00", "2007-02-19 00:00:00", "2007-04-06 00:00:00", "2007-05-28 00:00:00", "2007-07-04 00:00:00", "2007-09-03 00:00:00", "2007-11-22 00:00:00", "2007-12-25 00:00:00", "2008-01-01 00:00:00", "2008-01-21 00:00:00", "2008-02-18 00:00:00", "2008-03-21 00:00:00", "2008-05-26 00:00:00", "2008-07-04 00:00:00", "2008-09-01 00:00:00", "2008-11-27 00:00:00", "2008-12-25 00:00:00", "2009-01-01 00:00:00", "2009-01-19 00:00:00", "2009-02-16 00:00:00", "2009-04-10 00:00:00", "2009-05-25 00:00:00", "2009-07-03 00:00:00", "2009-09-07 00:00:00", "2009-11-26 00:00:00", "2009-12-25 00:00:00", "2010-01-01 00:00:00", "2010-01-18 00:00:00", "2010-02-15 00:00:00", "2010-04-02 00:00:00", "2010-05-31 00:00:00", "2010-07-05 00:00:00", "2010-09-06 00:00:00", "2010-11-25 00:00:00", "2010-12-24 00:00:00", "2010-12-31 00:00:00", "2011-01-17 00:00:00", "2011-02-21 00:00:00", "2011-04-22 00:00:00", "2011-05-30 00:00:00", "2011-07-04 00:00:00", "2011-09-05 00:00:00", "2011-11-24 00:00:00", "2011-12-26 00:00:00", "2012-01-02 00:00:00", "2012-01-16 00:00:00", "2012-02-20 00:00:00", "2012-04-06 00:00:00", "2012-05-28 00:00:00", "2012-07-04 00:00:00", "2012-09-03 00:00:00", "2012-11-22 00:00:00", "2012-12-25 00:00:00", "2013-01-01 00:00:00", "2013-01-21 00:00:00", "2013-02-18 00:00:00", "2013-03-29 00:00:00", "2013-05-27 00:00:00", "2013-07-04 00:00:00", "2013-09-02 00:00:00", "2013-11-28 00:00:00", "2013-12-25 00:00:00", "2014-01-01 00:00:00", "2014-01-20 00:00:00", "2014-02-17 00:00:00", "2014-04-18 00:00:00", "2014-05-26 00:00:00", "2014-07-04 00:00:00", "2014-09-01 00:00:00", "2014-11-27 00:00:00", "2014-12-25 00:00:00", "2015-01-01 00:00:00", "2015-01-19 00:00:00", "2015-02-16 00:00:00", "2015-04-03 00:00:00", "2015-05-25 00:00:00", "2015-07-03 00:00:00", "2015-09-07 00:00:00", "2015-11-26 00:00:00", "2015-12-25 00:00:00", "2016-01-01 00:00:00", "2016-01-18 00:00:00", "2016-02-15 00:00:00", "2016-03-25 00:00:00", "2016-05-30 00:00:00", "2016-07-04 00:00:00", "2016-09-05 00:00:00", "2016-11-24 00:00:00", "2016-12-26 00:00:00", "2017-01-02 00:00:00", "2017-01-16 00:00:00", "2017-02-20 00:00:00", "2017-04-14 00:00:00", "2017-05-29 00:00:00", "2017-07-04 00:00:00", "2017-09-04 00:00:00", "2017-11-23 00:00:00", "2017-12-25 00:00:00", "2018-01-01 00:00:00", "2018-01-15 00:00:00", "2018-02-19 00:00:00", "2018-03-30 00:00:00", "2018-05-28 00:00:00", "2018-07-04 00:00:00", "2018-09-03 00:00:00", "2018-11-22 00:00:00", "2018-12-25 00:00:00", "2019-01-01 00:00:00", "2019-01-21 00:00:00", "2019-02-18 00:00:00", "2019-04-19 00:00:00", "2019-05-27 00:00:00", "2019-07-04 00:00:00", "2019-09-02 00:00:00", "2019-11-28 00:00:00", "2019-12-25 00:00:00", "2020-01-01 00:00:00", "2020-01-20 00:00:00", "2020-02-17 00:00:00", "2020-04-10 00:00:00", "2020-05-25 00:00:00", "2020-07-03 00:00:00", "2020-09-07 00:00:00", "2020-11-26 00:00:00", "2020-12-25 00:00:00", "2021-01-01 00:00:00", "2021-01-18 00:00:00", "2021-02-15 00:00:00", "2021-04-02 00:00:00", "2021-05-31 00:00:00", "2021-07-05 00:00:00", "2021-09-06 00:00:00", "2021-11-25 00:00:00", "2021-12-24 00:00:00", "2021-12-31 00:00:00", "2022-01-17 00:00:00", "2022-02-21 00:00:00", "2022-04-15 00:00:00", "2022-05-30 00:00:00", "2022-07-04 00:00:00", "2022-09-05 00:00:00", "2022-11-24 00:00:00", "2022-12-26 00:00:00",
                ]

    not_counted_days += holidays

    print("all_dates: ", type(all_dates.to_list()))

    print("not_counted_days: ", type(not_counted_days))

    #dtes = all_dates.to_list().difference(not_counted_days)

    #dates = list(set(all_dates.to_list()) - set(not_counted_days))
    dates = list(set(all_dates_arr) - set(not_counted_days))

    """
    
    THIS DATE ARRAY IS WHAT IS NEEDED TO BE THE INDEX FOR COLUMNS

    """

    print(dates)


if __name__ == "__main__":
    main()
