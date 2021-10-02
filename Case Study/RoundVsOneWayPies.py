import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Main_Trips_2019.csv', header=0, names=['start_time', 'seconds_duration', 'start_station_name', 'end_station_name', 'user_type', 'gender', 'birth_year'], usecols=[ 'start_time', 'start_station_name', 'end_station_name', 'user_type'], thousands=',')
df.dropna()

#Convert Columns to new columns
df['start_time'] = pd.to_datetime(df['start_time'], format='%Y-%m-%d %H:%M:%S')

#Subscriber Descriptive Data.
sub_df = df.where(df['user_type'] == 'Subscriber')
print('Sub count\n', sub_df.count())
sub_df.dropna()

#Customer Descriptive Data.
cust_df = df.where(df['user_type'] == 'Customer')
print('Cust count\n', cust_df.count())
cust_df.dropna()

print('Getting data frames of Same Station vs Different Station trips')

cust_same_station = cust_df.where(cust_df['start_station_name'] == cust_df['end_station_name'])
cust_same_station.dropna()
cust_diff_station = cust_df.where(cust_df['start_station_name'] != cust_df['end_station_name'])
cust_diff_station.dropna()
print('Cust Count Same+Diff \n', (cust_same_station.count() + cust_diff_station.count()))

sub_same_station = sub_df.where(sub_df['start_station_name'] == sub_df['end_station_name'])
sub_same_station.dropna()
sub_diff_station = sub_df.where(sub_df['start_station_name'] != sub_df['end_station_name'])
sub_diff_station.dropna()
print('Sub Count Same+Diff \n', (sub_same_station.count() + sub_diff_station.count()))

print('Getting trip counts for customers & subscribers')
cust_same_station_trips = pd.DataFrame(cust_same_station['start_time'].groupby(cust_same_station['start_station_name']).count())
cust_diff_station_trips = pd.DataFrame(cust_diff_station['start_time'].groupby(cust_diff_station['start_station_name']).count())
sub_same_station_trips = pd.DataFrame(sub_same_station['start_time'].groupby(sub_same_station['start_station_name']).count())
sub_diff_station_trips = pd.DataFrame(sub_diff_station['start_time'].groupby(sub_diff_station['start_station_name']).count())


print('\nCustomer')
# print('\nCust_Same ', cust_same_station_trips['start_time'].sum())
# print('\nCust_Diff ', cust_diff_station_trips['start_time'].sum())
# print('Customer Same Station Trips Description ', cust_same_station_trips.describe())
# print('Customer Diff Station Trips Description ', cust_diff_station_trips.describe())
# print('Customer Same Station Count ', cust_same_station.count())
# print('Customer Diff Station Count ', cust_diff_station.count())
cust_same_total = cust_same_station_trips['start_time'].sum()
cust_diff_total = cust_diff_station_trips['start_time'].sum()
# print('Customer Same Station Total Trips ', cust_same_total)
# print('Customer Diff Station Total Trips ', cust_diff_total)

print('\nSubscriber')
# print('\nSub_Same ', sub_same_station_trips['start_time'].sum())
# print('\nSub_Diff ', sub_diff_station_trips['start_time'].sum())
# print('Subscriber Same Station Trips Description ', sub_same_station_trips.describe())
# print('Subscriber Same Station Count ', cust_same_station.count())
# print('Subscriber Diff Station Trips Description ', sub_diff_station_trips.describe())
# print('Subscriber Diff Station Count ', sub_same_station.count())
sub_same_total = sub_same_station_trips['start_time'].sum()
sub_diff_total = sub_diff_station_trips['start_time'].sum()
# print('Subscriber Same Station Total Trips ', sub_same_total)
# print('Subscriber Diff Station Total Trips ', sub_diff_total)

cust_total = cust_same_total + cust_diff_total
sub_total = sub_same_total + sub_diff_total

cust_same_pct = (cust_same_total / cust_total) * 100
cust_diff_pct = (cust_diff_total / cust_total) * 100

sub_same_pct = (sub_same_total / sub_total) * 100
sub_diff_pct = (sub_diff_total / sub_total) * 100

print('Setting up Chart.')

pie_labels = ['One Way', 'Round Trip']
cust_sizes = [cust_diff_pct, cust_same_pct]
sub_sizes = [sub_diff_pct, sub_same_pct]

fig, ax = plt.subplots()

# Subscriber Trip Chart Set Up
ax.set_title('Subscriber Trip Types')
ax.pie(sub_sizes, labels=pie_labels, autopct='%1.1f%%', startangle=0)

# # Customer Trip Chart Set Up
# ax.set_title('Customer Trip Types')
# ax.pie(cust_sizes, labels=pie_labels, autopct='%1.1f%%', startangle=0)

ax.axis('equal')

plt.show()

