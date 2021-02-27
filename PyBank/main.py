import os
import os.path
import csv
current_directory = os.path.dirname(__file__)
budget_csv = os.path.join(current_directory, 'Resources', 'budget_data.csv')

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    month=[]
    profit=[]
    p_change=[]

    csv_header = next(csv_file)
   
    for row in csv_reader:
        month.append(row[0])
        profit.append(int(row[1]))
    for i in range ((len(profit)-1)):
       p_change.append(profit[i+1]-profit[i])

    max_inc=max(p_change)
    max_dec=min(p_change)

    max_inc_month=month[(p_change.index(max(p_change))+1)]
    max_dec_month=month[(p_change.index(min(p_change))+1)]

print("Financial Analysis")
print("----------------------")
print(f"Total Months: {len(month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(p_change)/len(p_change),2)}")
print(f"Greatest Increase in Profits: {max_inc_month} (${(str(max_inc))})")
print(f"Greatest Decrease in Profits: {max_dec_month} (${(str(max_dec))})")

output_path = os.path.join(current_directory,"analysis","Summary.csv")

with open(output_path,"w",newline='') as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(month)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(p_change)/len(p_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_inc_month} (${(str(max_inc))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {max_dec_month} (${(str(max_dec))})")
