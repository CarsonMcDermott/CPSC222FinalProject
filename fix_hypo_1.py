## file to fix/clean data for hypothesis testing 1 of final project
## CPSC 222


import pandas as pd
import numpy as np

## read in the data file
streams_df1 = pd.read_csv("StreamingHistory.csv")   # loaded in Jaylene's data

## change the date to per day
## use the classifier from last DA to change these dates to numeric?
        # pretty sure already wrote code similar to this
streams_df1[ "WK" ] = pd.to_datetime(streams_df1["endTime"]).dt.isocalendar().week     #  reference: https://techtrekking.com/how-to-convert-daily-time-series-data-into-weekly-and-monthly-using-pandas-and-python/
print("***", streams_df1, "***")              # test
streams_df1["endTime"] = streams_df1["WK"]
streams_df1.drop(["WK"], axis=1)
print(streams_df1)              # test
streams_df1.to_csv("YAY_Jaylene.csv", index= False)
streams_df1.drop("WK", inplace=True, axis=1)
streams_df1.to_csv("YAY_Jaylene.csv", index= False)
## CODE REFERENCE
## link: https://www.geeksforgeeks.org/extract-week-number-from-date-in-pandas-python/
## another link: https://www.geeksforgeeks.org/convert-json-to-csv-in-python/

# importing pandas as pd
# import pandas as pd 
  
# # creating a dictionary containing a date
# dict = streams_df1["endTime"]
  
# # converting the dictionary to a dataframe
# df = pd.DataFrame.from_dict(dict)
  
# # converting the date to the required format
# df['endTime'] = pd.to_datetime(df['endTime'], errors ='coerce')
# df.astype('int64').dtypes
  
# # extracting the week from the date
# weekNumber = df['endTime'].dt.week
  
# print(weekNumber)
# df["endTime"] = weekNumber
# print(df["endTime"])

# streams_df2 = streams_df1.to_csv("StreamingHistory_updated.csv", index = False)
# ## CODE REFERENCE






## take in the cleaned data for weeks, calulate the percentage of pop listened to per weeks
# the artists the correspond to pop are:
# (FOR  JAYLENE DATA) = Taylor Swift, Olivia Rodrigo, 5 Seconds of Summer, Britney Spears
# (FOR CARSON DATA) = 

# create a loop to walk through each data point and say "if it's from this artist, then plus 1 to a count"
# take that count value, and divide it by len(data_set) * 100 = percentage of pop listened to per week

## total percent of pop
pop_artists_jaylene = ["Taylor Swift", "Olivia Rodrigo", "5 Seconds of Summer", "Britney Spears"]
count = 0
for i in streams_df1["artistName"]:
        if i in pop_artists_jaylene:
                count += 1
total_percent_of_pop = count/len(streams_df1["artistName"]) * 100
print(total_percent_of_pop)             # will print jaylene total = 23.59%

count2 = 0
## percent of pop by week





