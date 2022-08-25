import os
import csv
os.chdir(os.path.("Resources/budget_data.csv"))



total_months = 0
total_revenue = 0
previous_revenue = 0
revenue = []
month_change = []
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
revenue_change_list = []
revenue_average = 0

with open('budget_data.csv') as csv

loop to find total month for row in csvrader:
total_months +=1

total_revenue = total_revenue + row("Profit/Losses")

revenue_change = float(row["Profit/Losses"]) - previous_revenue

previous_revenue = flo(row["profit/Losses"])
revenue_change_list = revenue_change_list +[revenue_change]
month_change = month_change + [row["Date"]]


greatest_increase
if revenue_change>greatest_increase[1]:
    greatest_increase[1] = revenue_change
    greatest_increase[0] = row["Date"]



    greatest_decrease
    if revenue_change<greatest_decrease
    greatest_decrease[1] = revenue_change
    greatest_decrease[0] = row["Date"]

    revenue_average =  sum(revenue_change_list)/len(revenue_change_list)


with open(text_path, 'W') as file:

    print("financial analysis\n")
    print("----------------\n")
    print("Total Months: %d\n" % total_months)
    print("Total Revenue: $%d\n" % total_revenue)
    print("Average Revenue Change $%d\n" % revenue_change_list)
    print("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
    

    

    

