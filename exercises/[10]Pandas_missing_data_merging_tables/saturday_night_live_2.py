import pandas as pd

snl = pd.read_csv('https://github.com/gdv/foundationsCS/raw/main/students/ex-data/snldb/snl_title.csv')
print(snl.head())

episodes = pd.read_csv('https://github.com/gdv/foundationsCS/raw/main/students/ex-data/snldb/snl_episode.csv', parse_dates=["aired"])
print(episodes.head())

seasons = pd.read_csv('https://github.com/gdv/foundationsCS/raw/main/students/ex-data/snldb/snl_season.csv')
#print(seasons.head())

ratings = pd.read_csv('https://github.com/gdv/foundationsCS/raw/main/students/ex-data/snldb/snl_rating.csv')
print(ratings.head())


# Exercise 1
# Compute the sketches of the season with year 1978

selected_rows = pd.merge(snl, seasons, left_on = 'sid', right_on='sid')
output = selected_rows[(selected_rows['year'] == 1977) & (selected_rows['titleType'] == 'Sketch')]


# Exercise 2
# Compute the sketches of the seasons with year 1978-1982

output = selected_rows[(selected_rows['year'] >= 1978) & (selected_rows['year'] <= 1982) & (selected_rows['titleType'] == 'Sketch')]


# Exercise 3
# Compute the sketches aired in 1978 (consider the table snl_episode.csv)

snl_sketch = snl[snl['titleType'] == 'Sketch']
selected_rows = pd.merge(snl_sketch, episodes, on = ['sid','eid'], how='inner')

output = selected_rows[selected_rows['aired'].dt.year == 1978]


# Exercise 4
# For each season, compute the average number of top 1000 voters

output = ratings.groupby('sid').mean()['Top 1000 voters']


# Exercise 5
# For each season, compute the difference between the maximum and the minimum of US users_avg

min = ratings.groupby('sid').min()['US users_avg']
max = ratings.groupby('sid').max()['US users_avg']
output = pd.merge(max, min, on = 'sid', how='inner', suffixes=['_max', '_min'])

output['diff_max_min'] = output['US users_avg_max'] - output['US users_avg_min']

print(output)
