import grab_data_func from "./dataGrab.py"
import reshape_data_func from "./reshapeData.py"

def main():
  
  """
 
 1. grab data with grab func.
 
 2. format the data with reshape func
 
 3. train with the data
 
  
  """
  
  dates = [
    ["2022-05-12 00:00:00", "2022-05-13 00:00:00"],
    ["2022-05-11 00:00:00", "2022-05-12 00:00:00"],
    ["2022-05-10 00:00:00", "2022-05-11 00:00:00"],
    ["2022-05-09 00:00:00", "2022-05-10 00:00:00"]
  ]
  
  URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=5min&slice=year1month1&apikey=KGNJMQQ0GZUCIB2R&datatype=csv"
  
  # grab data
  raw_data_arr = [] # array to store all data from diffrent time spans
  
  for time_interval in dates:
    raw_data_arr.append(grab_data_func(time_interval[0], time_interval[1], URL))
    
  # format data
  data_arr = []
  
  for raw_data in raw_data_arr:
    data_arr.append(reshape_data_func(raw_data))
  
if __main__ == "__main__":
  main()

