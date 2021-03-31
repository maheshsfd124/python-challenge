# importing various module
import os
import csv
election_candidate =[]
election_votes = []
election_csv = os.path.join('..','Resources', 'election_data.csv')
# opening csv file to get read in
with open(election_csv,newline ='', encoding='utf-8') as electionfile:
    election_input = csv.reader(electionfile,delimiter =",")
    election_header = next(election_input)
# iterating budget file to get month and amount  list
    

    for row in election_input:
        election_votes.append(row[0])
        election_candidate.append(row[2])
        total = len(election_votes)
    print(" Total number of votes casted : " + " " + str(len(election_votes)))
    print(" Total number of canidate index: " + " " + str(len(election_candidate)))
    # print (election_candidate[2])
ind =[]

# finding index to get index of amount list
count1 =0 
count2 =0
count3 =0
count4 =0
for x in election_candidate:
    if x == "Khan":
        count1 = count1 + 1
        count1per = count1/total *100
    elif x == "Correy":
        count2 = count2 + 1
        count2per = count2/total *100
    elif x == "Li":
        count3 = count3 + 1
        count3per = count3/total *100
    elif x == "O'Tooley":
        count4= count4 + 1
        count4per = count4/total *100

print(count1)
print(count2)
print(count3)
print(count4)
print (count1per)
print (count2per)
print (count3per)
print (count4per)

print("Election Results")
print("------------------------")
print ("Total Votes : " + " " + str(len(election_votes)))
print("------------------------")
print("Khan: " + " " + str(count1per) + "%" +" (" + str(count1) +")")
print("Correy: " + " " + str(count2per) + "%" +" (" + str(count2) +")")
print("Li: " + " " + str(count3per) + "%" +" (" + str(count3) +")")
print("O'Tooley: " + " " + str(count4per) + "%" +" (" + str(count4) +")")
         
 
 