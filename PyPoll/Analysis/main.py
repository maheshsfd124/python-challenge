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
    print(" Total number of votes casted : " + " " + str(len(election_votes)))
    print(" Total number of canidate index: " + " " + str(len(election_candidate)))
    print (election_candidate[2])
ind =[]

# finding index to get index of amount list
for count in election_votes:
    ind.append(election_votes.index(count))
print(ind)
# res ={}
# res = dict(zip(election_candidate,ind))
# print (str(res))

         
 
 