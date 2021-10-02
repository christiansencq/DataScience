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


#Customer Descriptive Data.
cust_df = df.where(df['user_type'] == 'Customer')
cust_df.dropna()
custTDmax = cust_df['time_duration'].max()
print('Cust Trip Duration Max ', custTDmax, '\n')
custTDmean = cust_df['time_duration'].mean()
print('Cust Trip Duration Mean ', custTDmean, '\n')
custDayMode = cust_df['weekday'].mode()
print('Cust Day Mode ', custDayMode, '\n')

print('\n\n\n')

day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#Get Mean Trip Duration for day of week.
weekday_trips = pd.DataFrame(df.groupby(df['weekday']).count())
weekday_trips['start_time'] = weekday_trips['start_time']/1000

# print('Wd_means  \n', weekday_means)
reind_weekday_trips = weekday_trips.reindex(day_order)
print('Wd_trips  \n', reind_weekday_trips)
print('WD Desc \n', reind_weekday_trips.describe())

x = np.arange(len(day_order))
width = 0.95

fig, ax = plt.subplots()
ax.set_ylabel('# of Trips (in 1000s)')
ax.set_title('Total Trips Taken By Day of Week')
ax.set_xticks(x)
ax.set_xticklabels(day_order)

ax.bar(x, reind_weekday_trips['start_time'], width, label='Weekday')

fig.tight_layout()

plt.show()

