import pandas as pd

# Exercise 1: read the files 2017_german_election_overall.csv and 2017_german_election_party.csv from the german-election-2017 dataset.
overalldata = pd.read_csv("https://github.com/gdv/foundationsCS/raw/main/students/ex-data/german-election-2017/2017_german_election_overall.csv")
partydata = pd.read_csv("https://github.com/gdv/foundationsCS/raw/main/students/ex-data/german-election-2017/2017_german_election_party.csv")
print(overalldata, partydata)

# Exercise 2: for each area, compute the percentage of the voters over the registered voters
print(overalldata['area_id'], overalldata['total_votes']/overalldata['registered.voters']*100)

# Exercise 3: for each state, compute the total number of registered voters
states = []
for state in overalldata['state']:
    if state not in states:
        states.append(state)

for state in states:
    registered_voters_sum =0
    for registered_voters in overalldata[overalldata['state']==state]['registered.voters']:
        registered_voters_sum += registered_voters
    print(state, registered_voters_sum)

# Exercise 4: how many registered voters are there in Bayern or Saarland (compute the voters in each state and the sum of the two numbers)
registered_voters_sum =0
for registered_voters in overalldata[overalldata['state'] == 'Saarland']['registered.voters']:
    registered_voters_sum += registered_voters
for registered_voters in overalldata[overalldata['state'] == 'Bayern']['registered.voters']:
    registered_voters_sum += registered_voters
print(registered_voters_sum)

# Exercise 5: for each state, compute the number of votes (first vote) for each party
parties = []
for party in partydata['party']:
    if party not in parties:
        parties.append(party)

for state in states:
    for party in parties:
        votes_sum = 0
        for d_votes in partydata[(partydata['state']==state) & (partydata['party']==party)]['votes_first_vote']:
            votes_sum += d_votes
        print(state, party, votes_sum)

# Exercise 6: For each state and each party, compute the area where the party has taken most total votes
partydata['total_votes'] = partydata['votes_first_vote'] + partydata['votes_second_vote']
for state in states:
    for party in parties:
        max_votes = 0
        for votes in partydata[(partydata['state']==state) & (partydata['party']==party)]['total_votes']:
            if votes > max_votes:
                max_votes = votes
        print(state, party, max_votes)
        print(partydata[(partydata['state']==state) & (partydata['party']==party) & (partydata['total_votes']==max_votes)]['area_id'])
