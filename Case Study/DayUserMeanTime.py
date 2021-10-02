import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, date2num

df = pd.read_csv('Main_Trips_2019.csv', header=0, names=['start_time', 'seconds_duration', 'user_type', 'gender', 'birth_year'], usecols=[ 'start_time', 'seconds_duration', 'user_type'], thousands=',')
df.dropna()


day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#Convert Columns to new columns
df['start_time'] = pd.to_datetime(df['start_time'], format='%Y-%m-%d %H:%M:%S')
df['weekday'] = df['start_time'].dt.day_name()
df['time_duration'] = pd.to_timedelta(df['seconds_duration'], unit='s')

#Subscriber Descriptive Data.
sub_df = df.where(df['user_type'] == 'Subscriber')
sub_df.dropna()

#Customer Descriptive Data.
cust_df = df.where(df['user_type'] == 'Customer')
cust_df.dropna()

print('\n\n\n')


sub_wd_means = pd.DataFrame(sub_df['time_duration'].groupby(sub_df['weekday']).mean())
sub_wd_means.dropna()
reind_sub_wd_means = sub_wd_means.reindex(day_order)
reind_sub_wd_means['time_duration'] = reind_sub_wd_means['time_duration'].dt.total_seconds()/60

cust_wd_means = pd.DataFrame(cust_df['time_duration'].groupby(cust_df['weekday']).mean())
cust_wd_means.dropna()
reind_cust_wd_means = cust_wd_means.reindex(day_order)
reind_cust_wd_means['time_duration'] = reind_cust_wd_means['time_duration'].dt.total_seconds()/60


#Set Up Chart
x = np.arange(len(day_order))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, reind_sub_wd_means['time_duration'], width, label='Subscribers')
rects2 = ax.bar(x + width/2, reind_cust_wd_means['time_duration'], width, label='Customers')

ax.set_ylabel('Mean Trip Duration (minutes)')
ax.set_title('Average Trip Duration By Weekday and Usertype')
ax.set_xticks(x)
ax.set_xticklabels(day_order)
ax.legend()

#Can add these for total labels on each Bar.
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)

plt.show()
