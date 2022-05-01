## file to fix/clean data for hypothesis testing 1 of final project
## CPSC 222


import pandas as pd
import numpy as np
import statistics

## read in the data file
streams_df1 = pd.read_csv("StreamingHistory.csv")   # loaded in Jaylene's data

## change the date to per day
## use the classifier from last DA to change these dates to numeric?
        # pretty sure already wrote code similar to this
streams_df1[ "WK" ] = pd.to_datetime(streams_df1["endTime"]).dt.isocalendar().week     #  reference: https://techtrekking.com/how-to-convert-daily-time-series-data-into-weekly-and-monthly-using-pandas-and-python/
# print("***", streams_df1, "***")              # test
streams_df1["endTime"] = streams_df1["WK"]
streams_df1.drop(["WK"], axis=1)
# print(streams_df1)              # test
streams_df1.to_csv("YAY_Jaylene.csv", index= False)
streams_df1.drop("WK", inplace=True, axis=1)
sorted_streams = streams_df1.sort_values(by='endTime', ascending=True)
print("***", sorted_streams)
# streams_df1.sort("endTime")	# test
sorted_streams.to_csv("YAY_Jaylene.csv", index= False)
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
print("Total Percent of Pop forom Jaylene's Spotify: ", total_percent_of_pop)             # will print jaylene total = 23.59%

## percent of pop by week
# grouping by week:
by_week = streams_df1.groupby("endTime")
# print(by_week.groups.keys())
# print(len(by_week.groups.keys()))               # there are 32 weeks in total

for group_name, group_df, in by_week:           # test, will print all the different tables made by the groupby (for J's data = 32 tables)
	group_name = group_name		# this code/assigning variables looks wonky but if want the individual graphs and their names, can print them
	group_df = group_df			# print this variable if you want the subtables
	# print()
	# 2. test to see how many of the pop aritist are in each table
	count = [i for i in group_df["artistName"] if i in pop_artists_jaylene]		# list comprehension
	# print("***", len(count))	# test
	percent_by_week = len(count)/len(group_df["artistName"]) * 100
	# print(group_name, percent_by_week)


## percentage of pop listened to per week by jaylene (rounded to three decimals): 
pop_percent_by_week = [12.477, 8.897, 19.551, 26.975, 42.222, 48.936, 45.3125, 51.672, 32.390, 35.227, 35.000, 30.285, 
					34.117, 27.714, 31.218, 31.718, 41.954, 38.071, 29.411, 28.715, 29.191, 23.828, 25.321, 16.576, 
					18.006, 18.945, 15.099, 15.642, 9.549, 13.243, 10.337, 9.369]
print(statistics.mean(pop_percent_by_week))		# mean = 26.780265625


# HYPOTHESIS TESTING:

# Note: according to: https://www.statology.org/left-tailed-test-vs-right-tailed-test/
	# Left-tailed test: The alternative hypothesis contains the “<” sign
	# Right-tailed test: The alternative hypothesis contains the “>” sign