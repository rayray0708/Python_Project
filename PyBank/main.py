import csv
import os
#path to csv file


csvpath= os.path.join("Resources","budget_data.csv")

total_month = 0
total_profit = 0
total_change = 0 #calculated by adding all the changes between 2 months together
change_in_month = 0 #total months
greatest_increase = 0 #value of greatest increase
#answer is a string here
greatest_increase_month ="Jan-10" #month at which greatest increase occurs
greatest_decrease = 0 #value of greatest decrease
#answer is a string here
greatest_decrease_month="Jan-10"#month at which greatest decrease occurs

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header=next(csv_reader)
    print("Header is:" + str(header))
    #during line 2, total_month is set to 1, profit is the value of line 2's profit, 
    # set previous profit to the value of row1's profit value
    Jan_row=next(csv_reader)
    #start calculating with the value of the second row
    total_profit= total_profit + int(Jan_row[1])
    total_month +=1 
    # print("January row is:" + str(Jan_row))
    prev_profit= int(Jan_row[1])

    for row in csv_reader:
        #sum of all rows lines starting from row 3 onwards
        total_month= total_month + 1
        #add the profit of the current row to the cumulative of previous profits
        total_profit= total_profit + int(row[1])
        change = int(row[1]) - prev_profit
        #sum of previous changes and the current row's change
        total_change += change
        change_in_month += 1 
        #set prev_profit to the current profit so that in the next calculation starts with a new value
        prev_profit = int(row[1])

        if change > greatest_increase:
            greatest_increase=change 
            greatest_increase_month=row[0]

        if change < greatest_decrease:
                greatest_decrease=change
                greatest_decrease_month=row[0]



# print(total_month) #total number of months
# print(total_profit) #total profit of 86 months
# print(total_change/change_in_month) #average change in profit
# print (greatest_increase)
# print(greatest_decrease)
# print(greatest_increase_month)
# print(greatest_decrease_month)

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: ${total_change/change_in_month:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""
#print total_month
#print total_profit
#print average change and round up to 2 decimal places
#print greatest increase in profits and associated month
#print greatest decrease in profits and associated month
print(output)

file = "Analysis/pyBank2.txt"

with open(file, 'w') as text_txt:
    text_txt.write(output)
