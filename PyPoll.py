import os   # a module that allows us to interact with our operating system
import csv 

# This time, we will read from a csv file and write the results to a new text file.

file_to_load = 'Resources/election_results.csv'
file_to_save = os.path.join('Analysis', 'election_results.txt')

total_votes = 0             # retrieve the total number of votes
list_of_candidates = []     # retrieve the list of unique candidates
candidate_votes = {}        # retrieve the total number of votes each candidate receives

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load, 'r') as election_data:

    # Use the built-in reader that came from the csv file in order to read election data
    file_reader = csv.reader(election_data)

    # Read the header first, because it's not part of our data.
    headers = next(election_data)
    #print(headers)

    """
        Total number of votes cast
        A complete list of candidates who received votes
        Total number of votes each candidate received
        Percentage of votes each candidate won
        The winner of the election based on popular vote

    Pseudocode for total number of votes cast:
        Create a variable to store the total number of votes.
        Open the data file.
        If applicable, read and ignore headers.
        Create a loop to increment the total number of votes.

    Pseudocode for a complete list of candidates who received votes:
        Create a variable to store the list of unique candidates.
        Open the data file.
        If applicable, read and ignore headers.
        Create a loop to read each row, and only care about the 3rd column.
        Add candidates onto our list if they are not already on there.
    
    Pseudocode for total number of votes each candidate received:
        Create a variable to store the dictionary of unique candidates.
        Open the data file.
        If applicable, read and ignore headers.
        Create a loop to read each row.
        If they are not on the list already, then add them and set vote value = 1.
        Otherwise, increment that candidate's vote count by 1.


    """

    # Read each row from the file reader 1 at a time
    for row in file_reader:
        total_votes += 1
        # print(row)

        # Each row is a list, and we want the candidate, which is on index 2
        # Check to see if candidate (row[2]) is not on our list
        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])   # add unique candidate to our list
            candidate_votes[row[2]] = 1         # candidate is key, num_votes = 1 is value
        # Otherwise, increment the key-value pair associated with the candidate by 1
        else:
            candidate_votes[row[2]] += 1        # increment by 1

print(f'The total number of votes cast is {total_votes}')
print(f'The list of candidates: {list_of_candidates}')
print(f'The number of votes each candidate received: {candidate_votes}')

"""
    Pseudocode to get the percentage of votes each candidate received:
        Retrieve the total number of votes
        Retrieve the number of votes each candidate received
        Loop through all key-value pairs in our dictionary
        For each key-value pair, calculate the percentage of votes and print it out
    
    Pseudocode to determine the winner of the election:
        Initialize the winning candidate as "" and their winning votes and percentages as 0
        Retrieve the total number of votes
        Retrieve the number of votes each candidate received
        Loop through all key-value pairs in our dictionary
        For each key-value pair, calculate the percentage of votes
            If the current candidate's vote is greater than the current winning votes
                AND if the current candidate's percentage is greater than the current winning percentage
                update the winning candidate and their winnings votes and percentages
        Print out the information of the winning candidate

"""
for candidate in candidate_votes.keys():
    percentage_votes = candidate_votes[candidate] / total_votes * 100
    print(f"{candidate}: received {percentage_votes:.2f}% of the vote.")

    # Check to see if the current candidate's number of votes and percentage of votes are greater than the current largest votes and percentages
    if candidate_votes[candidate] > winning_count and percentage_votes > winning_percentage:
        # Update the winning cadidate, winning vote, and winning percentage
        winning_candidate = candidate
        winning_count = candidate_votes[candidate]
        winning_percentage = percentage_votes

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.2f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


