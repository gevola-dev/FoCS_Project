import pandas as pd
import numpy as np

# Read the file access.log. This file is not trivial to read correctly

column_names = ["ip", "unknown1", "unknown2", "timestamp", "ms", "request", "status", "response_time"]

log = 'https://github.com/gdv/foundationsCS/raw/main/students/ex-data/apache/access.log'
log_df = pd.read_csv(log, sep=" ", header=None, names=column_names)

print(log_df)


# Count the number of accesses (number of lines) made by an IP number

IP_access_number = log_df.groupby('ip').size()

#print(IP_access_number)


# Count the number of successful accesses (status 200) made by an IP number

request_200 = log_df[log_df['status'] == 200]
IP_request_200 = request_200.groupby('ip').size()

#print(IP_request_200)


# Count the number of accesses for each directory served

log_df[['type', 'url']] = log_df['request'].str.extract(r'^(GET|POST|PUT)\s(.+)\sHTTP/\d\.\d$')

url_access_number = log_df.groupby('url').size()

#print(log_df)


# For each origin, count the number of successful accesses

request_200 = log_df[log_df['status'] == 200]

url_request_200 = request_200.groupby('url').size()

#print(url_request_200)


# For each origin, count the number of unsuccessful accesses, split according to the status code

request_not_200 = log_df[log_df['status'] != 200]

url_bad_requests = request_not_200.groupby(['url','status']).size()

#print(url_bad_requests)


# From the results of the previous point, add a column with the error class (the first digit of the status code)

log_df['error_class'] = np.where(log_df['status'] == 200, None, log_df['status'].astype(str).str[0])

#print(log_df)


# Cluster the accesses in 5-minutes time slices (e.g. from 14:00 to 14:05, from 14:05 to 14:10, etc). Count the number of accesses for each time slice

log_df['datetime'] = pd.to_datetime(log_df['timestamp'].str.strip('[]'), format='%d/%b/%Y:%H:%M:%S')

log_df['time_slice'] = log_df['datetime'].dt.floor('5T')

access_counts = log_df.groupby('time_slice').size()

print(access_counts)
