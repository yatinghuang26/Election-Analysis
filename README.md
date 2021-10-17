# Election-Analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to assist in the election audit process of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.


## Resources
- Data Source: election_results.csv
- Software: Python 3.10.1, Visual Studio Code, 1.61.1

## Summary
The analysis of the election results show:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Capser Stockham received 23.05% of all votes and 85,213 votes.
    - Diana DeGette received 73.81% of all votes and 272,892 votes.
    - Raymon Anthony Doane received 3.14% of all votes and 11,606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.81% of the vote and 272,892 votes.


## Challenge Overview
A Colorado Board of Elections employee has given the following tasks to assist in determining voter turnout of a recent local congressional election.

1. Determine how many votes each county casted.
2. Calculate each county's percentage of votes related to total votes.
3. Determine the county with the highest voter turnout.
4. Determine the number of votes associated with the county with the highest voter turnout.

## Challenge Summary
The summary of the voter turnout results show:
- The counties that voted were:
    - Jefferson
    - Denver
    - Arapahoe
- The voter turnout's results were:
    - Jefferson County casted 10.51% of all votes and 38,855 votes.
    - Denver County casted 82.78% of all votes and 306,055 votes.
    - Arapahoe County casted 6.71% of all votes and 24,801 votes.
- The county with the highest voter turnout was:
    - Denver County with 82.78% of all votes and 306,055 votes.

To use this method for all future elections, we would need to consider the format of the .csv file. This would affect where we would retrieve the needed information for our analysis.

```
        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

```
In this example, the indexes may need to change depending on the order of how the information is stored.

```
Ballot ID,County,Candidate

```
As seen above, this election results had the following format. However, this may change depending on how information is saved.
