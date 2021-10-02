import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
# import matplotlib.colors as mcolors
# import matplotlib._color_data as mcd
# from matplotlib.dates import DateFormatter, date2num


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
# cust_same_station_trips = pd.DataFrame(cust_same_station['start_time'].groupby(cust_same_station['start_station_name']))
# cust_diff_station_trips = pd.DataFrame(cust_diff_station['start_time'].groupby(cust_diff_station['start_station_name']))
# sub_same_station_trips = pd.DataFrame(sub_same_station['start_time'].groupby(sub_same_station['start_station_name']))
# sub_diff_station_trips = pd.DataFrame(sub_diff_station['start_time'].groupby(sub_diff_station['start_station_name']))


print('\nCustomer')
# print('\nCust_Same ', cust_same_station_trips['start_time'].sum())
# print('\nCust_Diff ', cust_diff_station_trips['start_time'].sum())
print('Customer Same Station Trips Description ', cust_same_station_trips.describe())
print('Customer Same Station Count ', cust_same_station.count())
# print('Customer Same Station Total Trips ', cust_same_station_trips['start_time'].sum())
print('Customer Diff Station Trips Description ', cust_diff_station_trips.describe())
print('Customer Diff Station Count ', cust_diff_station.count())
# print('Customer Diff Station Total Trips ', cust_diff_station_trips['start_time'].sum())

print('\nSubscriber')
# print('\nSub_Same ', sub_same_station_trips['start_time'].sum())
# print('\nSub_Diff ', sub_diff_station_trips['start_time'].sum())
print('Subscriber Same Station Trips Description ', sub_same_station_trips.describe())
print('Subscriber Same Station Count ', cust_same_station.count())
# print('Subscriber Same Station Total Trips ', sub_same_station_trips['start_time'].sum())
print('Subscriber Diff Station Trips Description ', sub_diff_station_trips.describe())
print('Subscriber Diff Station Count ', sub_same_station.count())
# print('Subscriber Diff Station Total Trips ', sub_diff_station_trips['start_time'].sum())

print('Sorting Data frames')
cust_top_station_round_trip = cust_same_station_trips.sort_values('start_time', ascending=False).head(10)
cust_top_station_one_way_trip = cust_diff_station_trips.sort_values('start_time', ascending=False).head(10)
cust_top_station_round_trip.rename(columns={'start_time':'num_trips'}, inplace=True)
cust_top_station_one_way_trip.rename(columns={'start_time':'num_trips'}, inplace=True)
cust_top_station_round_trip.reset_index(inplace=True)
cust_top_station_one_way_trip.reset_index(inplace=True)

sub_top_station_round_trip = sub_same_station_trips.sort_values('start_time', ascending=False).head(10)
sub_top_station_one_way_trip = sub_diff_station_trips.sort_values('start_time', ascending=False).head(10)
sub_top_station_round_trip.rename(columns={'start_time':'num_trips'}, inplace=True)
sub_top_station_one_way_trip.rename(columns={'start_time':'num_trips'}, inplace=True)
sub_top_station_round_trip.reset_index(inplace=True)
sub_top_station_one_way_trip.reset_index(inplace=True)

print()
# print("CustSameStation head sorted \n", cust_top_station_round_trip)
# print("CustSame Index \n", cust_top_station_round_trip.index)
# print("CustDiffStation head sorted \n", cust_top_station_one_way_trip)
# print("CustDiff Index \n", cust_top_station_one_way_trip.index)
print()

print()
# print("SubSameStation head sorted \n", sub_top_station_round_trip)
# print("SubSame Index \n", sub_top_station_round_trip.index)
# print("SubDiffStation head sorted \n", sub_top_station_one_way_trip)
# print("SubDiff Index \n", sub_top_station_one_way_trip.index)
print()

column_labels = ['Station Names', 'Trips']
colors = ['r', 'r']
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

# ax.set_title('Ten Most Used Stations For Round-Trip Customers')
# table = ax.table(cellText=cust_top_station_round_trip.values, cellLoc='center', colWidths=[0.65, 0.35], colLabels=column_labels, loc='center')

# ax.set_title('Ten Most Used Stations For One-Way Customers')
# table = ax.table(cellText=cust_top_station_one_way_trip.values, cellLoc='center', colWidths=[0.65, 0.35], colLabels=column_labels, loc='center')

# ax.set_title('Ten Most Used Stations For Round-Trip Subscribers')
# table = ax.table(cellText=sub_top_station_round_trip.values, cellLoc='center', colWidths=[0.65, 0.35], colLabels=column_labels, loc='center')

# ax.set_title('Ten Most Used Stations For One-Way Subscribers')
# table = ax.table(cellText=sub_top_station_one_way_trip.values, cellLoc='center', colWidths=[0.65, 0.35], colLabels=column_labels, loc='center')


# plt.show()
