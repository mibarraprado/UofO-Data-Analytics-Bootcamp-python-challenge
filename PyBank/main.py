#import os and csv modules to read data on the csv files
import os
import csv

#variables to store data
Totalmonths = 0
Total = 0
Average_Change = 0
p_l_value = 0
values=[]
dates =[]
changes = []
Greatest_increase = []
Greatest_decrease = []

#getting path to the current directory where main.py file is stored
current_directory = os.getcwd()
#path to the data file 
csvpath = os.path.join(current_directory, "Resources", "budget_data.csv")
#path to the output file
outputfile = os.path.join(current_directory,"analysis", "budget_data_analysis.txt")

#open CSV file where data is stored
with open(csvpath, encoding='utf') as csvfile:
    #read csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    #read header
    csv_header = next(csvfile)

    #for loop to read data rows in the csv file
    for row in csvreader:
        # get the profit/loss value for each month (inc row [1])
        p_l_value = int(row[1])
        # calculate net profit
        Total= Total+p_l_value
        #caculate total months in data ser
        Totalmonths=Totalmonths+1
        # store profit/loss values  and dates in a list
        values.append(row[1])
        dates.append(row[0])

#for loop to calculate montly changes and store the values of the monthly changes in a list 
for i in range(len(values)):
    if i != 0:
        changes.append(int(values[i])- int(values[i-1]))

#calculate average change
Average_Change = round(sum(changes)/len(changes),2)
#calculate max change
Greatest_increase.append(max(changes))
#get date of max change
Greatest_increase.append(dates[changes.index(max(changes))+1])
#calculate min change
Greatest_decrease.append(min(changes))
#get date of min change 
Greatest_decrease.append(dates[changes.index(min(changes))+1])

#generate the output list that contains the Financial Analysis. Each item in the list is a line that will written in the output file
output = ["Financial Analysis \n",
"----------------------------\n", f"Total Months: {Totalmonths}\n", 
f"Total: ${Total}\n", 
f"Average Change: ${Average_Change}\n",
f"Gratest Increase in Profits: {Greatest_increase[1]} (${Greatest_increase[0]})\n",
f"Gratest Decrease in Profits: {Greatest_decrease[1]} (${Greatest_decrease[0]})"]

# write output file
with open(outputfile,"w") as analysis:
    for line in output:
       analysis.write(line)