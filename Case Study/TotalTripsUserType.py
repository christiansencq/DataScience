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
total = df['start_time'].count()
print('Total ', total)


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
sub_total = sub_df['start_time'].count()
print('Sub Total Trips ', sub_total)

#Customer Descriptive Data.
cust_df = df.where(df['user_type'] == 'Customer')
cust_df.dropna()
cust_total = cust_df['start_time'].count()
print('Cust Total Trips ', cust_total)

pie_labels = ['Subscribers', 'Customers']

sub_pct = sub_total/total*100
cust_pct = cust_total/total*100

sizes = [sub_pct, cust_pct]

fig, ax = plt.subplots()
ax.set_title("Trips Taken By User Type")
ax.pie(sizes, labels=pie_labels, autopct='%1.1f%%', startangle=0)

ax.axis('equal')

plt.show()

print('\n\nDone\n')
