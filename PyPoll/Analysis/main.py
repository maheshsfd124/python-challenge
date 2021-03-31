# importing various module
import os
import csv
import sys
original_stdout = sys.stdout
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
output = []
for y in election_candidate:
    if y not in output:
        output.append(y)
print(output) 
# finding index to get index of amount list
count1 =0 
count2 =0
count3 =0
count4 =0
votes =[]
for x in election_candidate:
    # for y in output:
    if x == output[0]:
        count1 = count1 + 1
        count1per = count1/total *100
        
    elif x == output[1]:
        count2 = count2 + 1
        count2per = count2/total *100
        
    elif x == output[2]:
        count3 = count3 + 1
        count3per = count3/total *100
        
    elif x == output[3]:
        count4= count4 + 1
        count4per = count4/total *100
        

votes.append(count1)
votes.append(count2)
votes.append(count3)
votes.append(count4)

print(votes)
# print(count2)
# print(count3)
# print(count4)
# print (count1per)
# print (count2per)
# print (count3per)
# print (count4per)

res = {}
for key in output:
    for value in votes:
        res[key] = value
        votes.remove(value)
        break  
  
# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))

# a_dictionary = {"a": 1, "b": 2, "c": 3}

max_key = max(res, key=res.get)
all_values = res.values()
max_value = max(all_values)

print(max_key,max_value)

print("Election Results")
print("------------------------")
print ("Total Votes : " + " " + str(len(election_votes)))
print("------------------------")
print(output[0]  + " " + str(count1per) + "%" +" (" + str(count1) +")")
print(output[1]  + " " + str(count2per) + "%" +" (" + str(count2) +")")
print(output[2]  + " " + str(count3per) + "%" +" (" + str(count3) +")")
print(output[3]  + " " + str(count4per) + "%" +" (" + str(count4) +")")
print ("Winner: " + " " + max_key)
     
 
 # Writing back to txt file all output 
with open('new.txt','w') as f:
    sys.stdout = f
    print("Election Results")
    print("------------------------")
    print ("Total Votes : " + " " + str(len(election_votes)))
    print("------------------------")
    print(output[0]  + " " + str(count1per) + "%" +" (" + str(count1) +")")
    print(output[1]  + " " + str(count2per) + "%" +" (" + str(count2) +")")
    print(output[2]  + " " + str(count3per) + "%" +" (" + str(count3) +")")
    print(output[3]  + " " + str(count4per) + "%" +" (" + str(count4) +")")
    print ("Winner: " + " " + max_key)
    sys.stdout = original_stdout