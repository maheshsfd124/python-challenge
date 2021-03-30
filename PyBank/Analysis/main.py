import os
import csv
import sys
original_stdout = sys.stdout
budget_month =[]
budget_amount =[]
budget_csv = os.path.join('..','Resources', 'budget_data.csv')
with open(budget_csv,newline ='', encoding='utf-8') as budgetfile:
    budget_input = csv.reader(budgetfile,delimiter =",")
    budget_header = next(budget_input)
    for row in budget_input:
        budget_month.append(row[0])
        budget_amount.append(row[1])
    # print(budget_month)
    # print(budget_amount)
    total_months =len(budget_month)
    print("Total number of months in dataset are: " + str (total_months))
total = 0
for amount in budget_amount:
    total = total + float(amount)
print("total " + str (total))
ind =[]
change =[]
for amount in budget_amount:
    ind.append(budget_amount.index(amount))
# print(ind)
diff =[]
x=1
for x in ind:
    diff.append(float(budget_amount[x])-float(budget_amount[x-1]))
# print (diff)
length_diff =len(diff)
# print(length_diff)
totaldiff = 0
for amt in diff:
    totaldiff = (totaldiff + float(amt))
totaldiff1 = totaldiff - 196785.0
averdiff = totaldiff1/(length_diff-1)
print("Average Change: " + str(averdiff))
# print(max(diff))
# print(diff.index(1926159.0))
print("Greatest Increase in Profits: " + " " + str(budget_month[25]) +" ( $" + str(max(diff))+ ")" )
# print(min(diff))
# print(diff.index(-2196167.0))
# print(budget_month[44])
print("Greatest Decrease in Profits: " + " " + str(budget_month[44]) +" ( $" + str(min(diff))+ ")" )


# Specify the file to write to
output_path = os.path.join("result.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     # csvwriter.writerow(print("Greatest Decrease in Profits: " + " " + str(budget_month[44]) +" ( " + str(min(diff))+ ")" ))

#     # Write the second row
#     csv.writerow((print("Greatest Increase in Profits: " + " " + str(budget_month[25]) +" ( " + str(max(diff))+ ")" )))
with open('new.txt','w') as f:
    sys.stdout = f
    print(" Total number of months in dataset are: " + str (total_months))
    print("total " + str (total))
    print("Average Change: " + str(averdiff))
    print("Greatest Increase in Profits: " + " " + str(budget_month[25]) +" ( $" + str(max(diff))+ ")" )
    print("Greatest Decrease in Profits: " + " " + str(budget_month[44]) +" ( $" + str(min(diff))+ ")" )
    sys.stdout = original_stdout

