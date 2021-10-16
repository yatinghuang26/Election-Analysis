import os   # a module that allows us to interact with our operating system
import csv 

# This time, we will read from a csv file and write the results to a new text file.

file_to_load = 'Resources/election_results.csv'
file_to_save = os.path.join('Analysis', 'election_results.txt')

with open(file_to_load, 'r') as election_data:

    # Use the built-in reader that came from the csv file in order to read election data
    file_reader = csv.reader(election_data)

    # Read the header first, because it's not part of our data.
    headers = next(election_data)
    print(headers)

    # Read each row from the file reader 1 at a time
    for row in file_reader:
        print(row)
