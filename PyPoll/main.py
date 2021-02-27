import os
import os.path
import csv
current_directory = os.path.dirname(__file__)
election_csv = os.path.join(current_directory, 'Resources', 'election_data.csv ')
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    votes_total=0
    name=[]
    vote_count={}
    Summary={}

    csv_header = next(csv_file)
   
    for row in csv_reader:
        votes_total += 1
        if row[2] in name and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1
        
        else:
            name.append(row[2])
            vote_count[row[2]] = 1


for key,value in vote_count.items():
    Summary[key] = str(round((value/votes_total)*100,3)) + "% ("+str(value)+ ")"


winner = max(vote_count.keys(), key=(lambda k: vote_count[k]))


print('Election Results')
print('--------------------------------')
print(f'Total Votes: {votes_total}')
print('--------------------------------')
for kv in Summary.items():
    print( kv[0],':',kv[1])
print('--------------------------------')
print(f'Winner: {winner}')
print('--------------------------------')

output_path = os.path.join(current_directory,"analysis","Summary.csv")

with open(output_path,"w",newline='') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {votes_total}")
    file.write("\n")
    for kv in Summary.items():
        file.write(kv[0]+"  :  "+ kv[1] + ("\n"))
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("----------------------------")