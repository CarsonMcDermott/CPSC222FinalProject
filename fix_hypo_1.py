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
print(total_percent_of_pop)             # will print jaylene total = 23.59%

## percent of pop by week
# grouping by week:
by_week = streams_df1.groupby("endTime")
# print(by_week.groups.keys())
# print(len(by_week.groups.keys()))               # there are 32 weeks in total

# for group_name, group_df, in by_week:           # test, will print all the different tables made by the groupby (for J's data = 32 tables)
#     print(group_name)	
#     print(group_df)
    # print()
	# 2. test to see how many of the pop aritist are in each table
for group_name, group in by_week:
	print(group_name)


## ORIGNINAL VERSION OF THIS CODE, WILL PRINT THE WRONG WEEK NUMBERS AND ALSO SOMETIMES SCREWS UP THE PERCENTAGES
# for i in group_df["artistName"]:
# 	if i in pop_artists_jaylene:
# 		count += 1
# 	by_week_percent_of_pop = count/len(streams_df1["artistName"]) * 100
# 	print("week num is:", group_name, "and percent is:", by_week_percent_of_pop)           
	# print(pd.unique(by_week_percent_of_pop))
	# print(by_week_percent_of_pop)

#     week_pop = group_df[i].mean()   # will give you a series representing all values in the population column. it is also part of the for loop so it will give all the means 
#     print(group_mean_pop)
# # 3. Combine the mean_pops into a pandas Series... before the for loop, do mean_pop_ser
#     mean_pop_ser[group_name] = group_mean_pop
#     print()
# mean_pop_ser.name = "Mean Population"  # give your mean_pop_ser a name
# print(mean_pop_ser)


