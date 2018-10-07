import csv
import os

# create path to csv file
csvpath=os.path.join('..','PyBank','budget_data.csv')

#lists for month and financial data
months = []
financials = []

#read csv file and create lists for data
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        financials.append(int(row[1]))

#find total number of months in the dataset
total_months = len(months)

#create variables for greatest increase and decrease  and set them equal to the first financial data entry
#set total profit = 0 
increase = financials[0]
decrease = financials[0]
total_financials = 0

#loop through financial data set and compare to get the greatest increase and decrease
#calculate net profit/losses
for r in range(len(financials)):
    if financials[r] >= increase:
        increase = financials[r]
        inc_month = months[r]
    elif financials[r] <= decrease:
        decrease = financials[r]
        dec_month = months[r]
    total_financials += financials[r]

#calculate average change in profit/losses
average_change = round(total_financials/total_months, 2)

#sets path for output file
output_dest = os.path.join("..", "PyBank", "output.txt")

#print out summary of above calulations into new output
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total: $' + str(total_financials) + '\n')
    writefile.writelines('Average Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + inc_month + ' ($' + str(increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + dec_month + ' ($' + str(decrease) + ')')

#opens outout in text file and print to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())