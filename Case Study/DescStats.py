import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, date2num

df = pd.read_csv('Main_Trips_2019.csv', header=0, names=['start_time', 'seconds_duration', 'user_type', 'gender', 'birth_year'], usecols=[ 'start_time', 'seconds_duration', 'user_type'], thousands=',')

df.dropna()

#Convert Columns to new columns
df['start_time'] = pd.to_datetime(df['start_time'], format='%Y-%m-%d %H:%M:%S')
df['weekday'] = df['start_time'].dt.day_name()
df['time_duration'] = pd.to_timedelta(df['seconds_duration'], unit='s')

print('DF head', df.head)
print('Total ', df['start_time'].count())

#Ride Length Descriptive Stats
TDmax = df['time_duration'].max()
SECmax = df['seconds_duration'].max()
print('Time Max ', TDmax, '\n')

TDmean = df['time_duration'].mean()
SECmean = df['seconds_duration'].mean()
print('Time Mean ', TDmean, '\n')

WEEKDAYmode = df['weekday'].mode()
print('Weekday Mode ', WEEKDAYmode, '\n')


#Subscriber Descriptive Data.
sub_df = df.where(df['user_type'] == 'Subscriber')
sub_df.dropna()
subTDmax = sub_df['time_duration'].max()
print('Sub Trip Duration Max ', subTDmax, '\n')
subTDmean = sub_df['time_duration'].mean()
print('Sub Trip Duration Mean ', subTDmean, '\n')
subDayMode = sub_df['weekday'].mode()
print('Sub Day Mode ', subDayMode, '\n')
print('Sub Total Trips ', sub_df['start_time'].count())

#Customer Descriptive Data.
cust_df = df.where(df['user_type'] == 'Customer')
cust_df.dropna()
custTDmax = cust_df['time_duration'].max()
print('Cust Trip Duration Max ', custTDmax, '\n')
custTDmean = cust_df['time_duration'].mean()
print('Cust Trip Duration Mean ', custTDmean, '\n')
custDayMode = cust_df['weekday'].mode()
print('Cust Day Mode ', custDayMode, '\n')
print('Cust Total Trips ', cust_df['start_time'].count())

print('\n\nDone\n')
