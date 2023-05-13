# Read the csv data
data = []
with open('election_data.csv', 'r') as file:
    for line in file:
        data.append(line.strip().split(','))

# The total number of votes cast
total_count = len(data) - 1  # Subtracting 1 to exclude the header row

# A complete list of candidates who received votes
candidate_list = list(set([row[2] for row in data[1:]]))

# The percentage of votes each candidate won and the total number of votes each candidate won
charles_vote = len([row for row in data[1:] if row[2] == 'Charles Casper Stockham'])
diana_vote = len([row for row in data[1:] if row[2] == 'Diana DeGette'])
raymon_vote = len([row for row in data[1:] if row[2] == 'Raymon Anthony Doane'])
charles_pcnt = charles_vote / total_count * 100
diana_pcnt = diana_vote / total_count * 100
raymon_pcnt = raymon_vote / total_count * 100

# The winner of the election based on popular vote
vote_counts = {'Charles Casper Stockham': charles_vote,
               'Diana DeGette': diana_vote,
               'Raymon Anthony Doane': raymon_vote}
winner = max(vote_counts, key=vote_counts.get)

# Election results report
print('Election Results')
print('-' * 20)
print('Total Votes: ' + str(total_count))
print('-' * 20)
print('Charles Casper Stockham: ' + str(charles_pcnt) + '% ' + str(charles_vote))
print('Diane DeGette: ' + str(diana_pcnt) + '% ' + str(diana_vote))
print('Raymon Anthony Doane: ' + str(raymon_pcnt) + '% ' + str(raymon_vote))
print('-' * 20)
print('Winner: ' + winner)
print('-' * 20)
