import pandas as pd
import datetime as dt
import numpy as np


"""

Need to rename, new_df to df, temp mistake

"""


reshape_data_func(URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv",
                  DAY_SPAN = [12, 13],
                 ):
  df = pd.read_csv(URL)

  now = dt.datetime.now()
  custom_time = dt.datetime(int(now.strftime("%Y")), int(now.strftime("%m")), (int(now.strftime("%d")) - 2))
  #custom_time = dt.datetime(int(now.strftime("%Y")), int(now.strftime("%m")), 11)

  new_df = df

  for index, row in df.iterrows(): # dropping all data that doesn't align with my set date above (custom_time)
    if custom_time > dt.datetime.strptime(row["time"], '%Y-%m-%d %H:%M:%S'):
      new_df.drop(index, inplace=True)
    if dt.datetime(int(now.strftime("%Y")), int(now.strftime("%m")), (int(now.strftime("%d")) - 1)) < dt.datetime.strptime(row["time"], '%Y-%m-%d %H:%M:%S'):
      new_df.drop(index, inplace=True)

  #flip dataframe
  new_df = new_df.loc[::-1].set_index(new_df.index)

  time_index = { "04:05": 0, "04:10": 1, "04:15": 2, "04:20": 3, "04:25": 4, "04:30": 5, "04:35": 6, "04:40": 7, "04:45": 8, "04:50": 9, "04:55": 10, "05:00": 11, "05:05": 12, "05:10": 13, "05:15": 14, "05:20": 15, "05:25": 16, "05:30": 17, "05:35": 18, "05:40": 19, "05:45": 20, "05:50": 21, "05:55": 22, "06:00": 23, "06:05": 24, "06:10": 25, "06:15": 26, "06:20": 27, "06:25": 28, "06:30": 29, "06:35": 30, "06:40": 31, "06:45": 32, "06:50": 33, "06:55": 34, "07:00": 35, "07:05": 36, "07:10": 37, "07:15": 38, "07:20": 39, "07:25": 40, "07:30": 41, "07:35": 42, "07:40": 43, "07:45": 44, "07:50": 45, "07:55": 46, "08:00": 47, "08:05": 48, "08:10": 49, "08:15": 50, "08:20": 51, "08:25": 52, "08:30": 53, "08:35": 54, "08:40": 55, "08:45": 56, "08:50": 57, "08:55": 58, "09:00": 59, "09:05": 60, "09:10": 61, "09:15": 62, "09:20": 63, "09:25": 64, "09:30": 65, "09:35": 66, "09:40": 67, "09:45": 68 , "09:50": 69, "09:55": 70, "10:00": 71, "10:05": 72, "10:10": 73, "10:15": 74, "10:20": 75, "10:25": 76, "10:30": 77, "10:35": 78, "10:40": 79, "10:45": 80, "10:50": 81, "10:55": 82, "11:00": 83, "11:05": 84, "11:10": 85, "11:15": 86, "11:20": 87, "11:25": 88, "11:30": 89, "11:35": 90, "11:40": 91, "11:45": 92, "11:50": 93, "11:55": 94, "12:00": 95, "12:05": 96, "12:10": 97, "12:15": 98, "12:20": 99, "12:25": 100, "12:30": 101, "12:35": 102, "12:40": 103, "12:45": 104, "12:50": 105, "12:55": 106, "13:00": 107, "13:05": 108, "13:10": 109, "13:15": 110, "13:20": 111, "13:25": 112, "13:30": 113, "13:35": 114, "13:40": 115, "13:45": 116, "13:50": 117, "13:55": 118, "14:00": 119, "14:05": 120, "14:10": 121, "14:15": 122, "14:20": 123, "14:25": 124, "14:30": 125, "14:35": 126, "14:40": 127, "14:45": 128, "14:50": 129, "14:55": 130, "15:00": 131, "15:05": 132, "15:10": 133, "15:15": 134, "15:20": 135, "15:25": 136, "15:30": 137, "15:35": 138, "15:40": 139, "15:45": 140, "15:50": 141, "15:55": 142, "16:00": 143, "16:05": 144, "16:10": 145, "16:15": 146, "16:20": 147, "16:25": 148, "16:30": 149, "16:35": 150, "16:40": 151, "16:45": 152, "16:50": 153, "16:55": 154, "17:00": 155, "17:05": 156, "17:10": 157, "17:15": 158, "17:20": 159, "17:25": 160, "17:30": 161, "17:35": 162, "17:40": 163, "17:45": 164, "17:50": 165, "17:55": 166, "18:00": 167, "18:05": 168, "18:10": 168, "18:15": 170, "18:20": 171, "18:25": 172, "18:30": 173, "18:35": 174, "18:40": 175, "18:45": 176, "18:50": 177, "18:55": 178, "19:00": 179, "19:05": 180, "19:10": 181, "19:15": 182, "19:20": 183, "19:25": 184, "19:30": 185, "19:35": 186, "19:40": 187, "19:45": 188, "19:50": 189, "19:55": 190, "20:00": 191,
  }
  
  #####   changing the time column to only include time    ######
  for index, row in new_df.iterrows():
    try:
      time_obj = dt.datetime.strptime(row["time"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
      continue

    time_string = time_obj.strftime("%H") + ":" + time_obj.strftime("%M")

    for time_from_time_index in time_index:
      if time_string == time_from_time_index:

        new_df.loc[index, "time"] = time_from_time_index

        #print(time_from_time_index)

  # Setting time column to be index
  new_df.set_index("time", inplace=True)
  
  # resetting the index to be a list [0:len(df)] instead of time markers
  df.reset_index(inplace=True)
  
  df = df[["open", "high", "low", "close", "volume"]].stack().to_frame() # stacking all data verticaly
  df.index = [f"{k}_{n}" for n,k in df.index] # name each index to have different indexes (eg, "open_0", "open_1", "open_2")

  df = df.swapaxes(0, 1, copy=True) # swap the axis to make the df column based instead of stacked
  print(df)
