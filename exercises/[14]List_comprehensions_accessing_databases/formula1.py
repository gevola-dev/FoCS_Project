import pandas as pd
import numpy as np

urls = {
    "circuits": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/circuits.csv",
    "circuits_bkp": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/circuits_bkp.csv",
    "constructorResults": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/constructorResults.csv",
    "constructorStandings": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/constructorStandings.csv",
    "constructors": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/constructors.csv",
    "driverStandings": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/driverStandings.csv",
    "drivers": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/drivers.csv",
    "drivers_bkp": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/drivers_bkp.csv",
    "lapTimes": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/lapTimes.csv",
    "pitStops": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/pitStops.csv",
    "qualifying": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/qualifying.csv",
    "races": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/races.csv",
    "results": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/results.csv",
    "seasons": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/seasons.csv",
    "status": "https://github.com/gdv/foundationsCS/raw/main/students/ex-data/f1-db/status.csv"
}

dataframes = {}

for name, url in urls.items():
    try:
        dataframes[name] = pd.read_csv(url, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        print("Encoding issue with file:", name)


# For each decade, compute who is the driver born in that decade that scored more points in his career.

dataframes["drivers"]['dob'] = pd.to_datetime(dataframes["drivers"]['dob'], format='%d/%m/%Y')
dataframes["drivers"]['birth_year'] = dataframes["drivers"]['dob'].dt.year
dataframes["drivers"]['decade'] = (dataframes["drivers"]['birth_year'] // 10) * 10

merged_df = dataframes["results"].merge(dataframes["drivers"][['driverId', 'decade']], on='driverId')

career_points = merged_df.groupby(['driverId', 'decade'])['points'].sum().reset_index()

top_driver_per_decade = career_points.loc[career_points.groupby('decade')['points'].idxmax()]

top_driver_details = top_driver_per_decade.merge(dataframes["drivers"], on='driverId')

print(top_driver_details)


# For each circuit, find the fastest lap and output it with: (1) the date it was perfomed, (2) the name of the driver, and (3) the lap time

lap_race_merged = dataframes["lapTimes"].merge(dataframes["races"][['raceId', 'circuitId', 'date']], on='raceId')

fastest_laps = lap_race_merged.loc[lap_race_merged.groupby('circuitId')['milliseconds'].idxmin()]

fastest_laps = fastest_laps.merge(dataframes["drivers"][['driverId', 'forename', 'surname']], on='driverId')

fastest_laps = fastest_laps[['circuitId', 'date', 'forename', 'surname', 'milliseconds']]

fastest_laps = fastest_laps.rename(columns={
    'date': 'date_performed',
    'forename': 'driver_forename',
    'surname': 'driver_surname',
    'milliseconds': 'lap_time'
})

print(fastest_laps)



# Find the driver that has spent the most time performing pit stops

# Sum the time spent in pit stops for each driver
pit_stop_times = dataframes['pitStops'].groupby('driverId')['milliseconds'].sum().reset_index()

# Find the driver with the maximum pit stop time
most_time_in_pit_stop = pit_stop_times.loc[pit_stop_times['milliseconds'].idxmax()]

# Get driver details
driver_details = dataframes['drivers'][dataframes['drivers']['driverId'] == most_time_in_pit_stop['driverId']]

# Combine the results
most_time_in_pit_stop = most_time_in_pit_stop.merge(driver_details, on='driverId')
print(most_time_in_pit_stop[['forename', 'surname', 'milliseconds']])


# For each nationality, find the driver that scored most points in their career

# Sum points for each driver
driver_points = dataframes['results'].groupby('driverId')['points'].sum().reset_index()

# Merge with driver details to get nationalities
driver_points = driver_points.merge(dataframes['drivers'][['driverId', 'nationality', 'forename', 'surname']], on='driverId')

# Find the driver with the most points for each nationality
top_driver_per_nationality = driver_points.loc[driver_points.groupby('nationality')['points'].idxmax()]

print(top_driver_per_nationality[['nationality', 'forename', 'surname', 'points']])


# Find the nations that have at least one driver with at least 1000 points

# Filter drivers with at least 1000 points
drivers_1000_points = driver_points[driver_points['points'] >= 1000]

# Find unique nationalities
nations_with_one_driver_1000_points = drivers_1000_points['nationality'].unique()

print("Nations with at least one driver scoring 1000 points or more:")
print(nations_with_one_driver_1000_points)


# Find the nations that have at least two drivers with at least 1000 points

# Count drivers with at least 1000 points by nationality
nationality_driver_counts = drivers_1000_points.groupby('nationality').size()

# Filter for nationalities with at least two such drivers
nations_with_two_drivers_1000_points = nationality_driver_counts[nationality_driver_counts >= 2].index.tolist()

print("Nations with at least two drivers scoring 1000 points or more:")
print(nations_with_two_drivers_1000_points)
