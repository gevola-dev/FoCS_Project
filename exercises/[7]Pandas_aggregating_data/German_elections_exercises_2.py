import pandas as pd

# Exercise 1: We first need to read the files `2017_german_election_overall.csv` and `2017_german_election_party.csv` from the german-election-2017 dataset.
german_overall = pd.read_csv("https://github.com/gdv/foundationsCS/raw/main/students/ex-data/german-election-2017/2017_german_election_overall.csv")
german_party = pd.read_csv("https://github.com/gdv/foundationsCS/raw/main/students/ex-data/german-election-2017/2017_german_election_party.csv")

# Exercise 2: For each state, compute the total number of registered voters.
german_overall.groupby('state').sum()['registered.voters']

# Exercise 3: How many registered voters are there in Bayern or Saarland (compute the voters in each state and the sum of the two numbers)
german_overall[german_overall['state'] == 'Bayern'].sum()['registered.voters'] + german_overall[german_overall['state'] == 'Saarland'].sum()['registered.voters']

# For each state, compute the number of votes (first vote) for each party
german_party.groupby('state').sum()['votes_first_vote']

# For each state and each party, compute the area where the party has taken the most total votes (first votes)
# Hint: using `max()` after a `groupby` returns the maximum **value** in the group, not the row that includes such value", "Therefore, we need to use `idxmax()`.
german_party.groupby(['state','party'])['votes_first_vote'].idxmax()

# For each party, compute the area where the party has taken the most and the least votes (first vote), as a percentage of the overall registered voters in the state.
grouped_party = german_party.groupby(['state','party']).agg(
    votes_first_vote_min = ('votes_first_vote','min'), 
    votes_first_vote_max = ('votes_first_vote','max'), 
    votes_first_vote_sum = ('votes_first_vote','sum'),
    votes_second_vote_sum = ('votes_second_vote','sum'))

grouped_party['perc_min'] = round(grouped_party['votes_first_vote_min'] / (grouped_party['votes_first_vote_sum'] + grouped_party['votes_second_vote_sum']) * 100, 2)
grouped_party['perc_max'] = round(grouped_party['votes_first_vote_max'] / (grouped_party['votes_first_vote_sum'] + grouped_party['votes_second_vote_sum']) * 100, 2)

# For each area, compute the difference between the valid first votes and the valid second votes
def diff_valid_votes(row):
    return abs(row['valid_first_votes'] - row['valid_second_votes'])

german_overall['diff_valid_votes'] = german_overall.apply(diff_valid_votes, axis = 1)

# For each party, compute the difference between the first votes and the second votes
def diff_votes(row):
    return abs(row['votes_first_vote'] - row['votes_second_vote'])

grouped_party = german_party.groupby('party').agg({'votes_first_vote':'sum','votes_second_vote':'sum'})
grouped_party['diff_votes'] = grouped_party.apply(diff_votes, axis = 1)

# For each state and each party, compute the difference between the first votes and the second votes
grouped_party = german_party.groupby(['state','party']).agg({'votes_first_vote':'sum','votes_second_vote':'sum'})
grouped_party['diff_votes'] = grouped_party.apply(diff_votes, axis = 1)

print(grouped_party)
