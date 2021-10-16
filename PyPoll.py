import os   # a module that allows us to interact with our operating system
import csv 

# This time, we will read from a csv file and write the results to a new text file.

file_to_load = 'Resources/election_results.csv'
file_to_save = os.path.join('Analysis', 'election_results.txt')

total_votes = 0   # retrieve the total number of votes
list_of_candidates = []     # retrieve the list of unique candidates

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
    """

    # Read each row from the file reader 1 at a time
    for row in file_reader:
        total_votes += 1
        # print(row)

        # Each row is a list, and we want the candidate, which is on index 2
        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])


print(f'The total number of votes cast is {total_votes}')
print(f'The list of candidates: {list_of_candidates}')


    
