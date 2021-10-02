import pandas as pd
import glob
import os

path = r'/home/charles/DataSci/PyWork/TrimTesting'
all_csv_files = glob.glob(os.path.join(path, "*.csv"))

li = []

#Append all of the dataframes.
for filename in all_csv_files:
    df = pd.read_csv(filename, header=0, names=['trip_id', 'start_time', 'end_time', 'bike_id', 'seconds_duration', 'start_station_id', 'start_station_name', 'end_station_id', 'end_station_name', 'user_type', 'gender', 'birth_year'], index_col=0, usecols=['trip_id', 'start_time', 'seconds_duration', 'start_station_name', 'end_station_name', 'user_type', 'gender', 'birth_year'], thousands=',')
    li.append(df)

#Concatenating all the frames into a single dataframe
frame = pd.concat(li, axis=0, ignore_index=True)

print("Frame head \n", frame.head)

#Export that to a new CSV file.
frame.to_csv("Main_Trips_2019.csv", index=False)


