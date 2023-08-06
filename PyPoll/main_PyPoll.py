import csv
import os

#path to csv file
csvpath_pypoll= os.path.join("Resources","election_data.csv")
# print(csvpath_pypoll)

Total_vote = 0
Stockham_count = 0
DeGette_count = 0
Doane_count=0
Stockham = "Charles Casper Stockham"
# print(Stockham)
DeGette = "Diana DeGette"
# print(DeGette)
Doane = "Raymon Anthony Doane"
# print(Doane)

with open(csvpath_pypoll, 'r') as csv_pypoll_file:
    csv_pypoll_reader = csv.reader(csv_pypoll_file, delimiter= ",")
    # print(csv_pypoll_reader)
    header_pypoll=next(csv_pypoll_reader)
    # print(header_pypoll)
    
    #start the for-loop here
    for row in csv_pypoll_reader:
        Total_vote += 1

        #if last value matches with variable Stockham's, then add 1 vote for Stockham
        if row[2] == Stockham:
            Stockham_count +=1
        #if last value matches with variable DeGette's, then add 1 vote for DeGette
        elif row [2] == DeGette:
            DeGette_count +=1
        #if last value matches with variable Doane's, then add 1 vote for Doane
        elif row [2] == Doane:
            Doane_count +=1



# print(Total_vote)
# print(Stockham_count)
# print(DeGette_count)
# print(Doane_count)
# print(Stockham_count/Total_vote)
# print(DeGette_count/Total_vote)
# print(Doane_count/Total_vote)

#calculate Stockham's vote percentage
Stockham_percentage = "{:.3%}".format(Stockham_count/Total_vote)
# print(Stockham_percentage)

#calculate DeGette's vote percentage
DeGette_percentage = "{:.3%}".format(DeGette_count/Total_vote)
# print(DeGette_percentage)

#calculate Doane's vote percentage
Doane_percentage = "{:.3%}".format(Doane_count/Total_vote)
# print(Doane_percentage)


output = f"""
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: {Stockham_percentage} ({Stockham_count})
Diana DeGette: {DeGette_percentage} ({DeGette_count})
Raymon Anthony Doane: {Doane_percentage} ({Doane_count})
-------------------------
Winner: Diana DeGette
-------------------------
"""

print(output)

file_txt_pypoll= "Analysis/pyPoll.txt"

with open(file_txt_pypoll, 'w') as pypoll_txt:
    pypoll_txt.write(output)
