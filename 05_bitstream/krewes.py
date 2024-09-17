#Victor Casado
#The Flying Mice
#SoftDev
#K05 -- Processing Bitstreams
#2024-09-17
#time spent: .5 hours
import random as r

f = open("krewes.txt", "r")
string = f.read()

number = 0
index = 0
dict = {}

while (index < len(string) - 1):

    pd = ""
    while(not (string[index] == '$')):
        pd += string[index]
        index += 1
    index += 3 #"skip" past the $s

    devo = ""
    while(not (string[index] == '$')):
        devo += string[index]
        index += 1
    index += 3 #"skip" past the $s

    ducky = ""
    while(not (string[index] == '@')):
        ducky += string[index]
        index += 1

    dict.update({number: [devo, pd, ducky]}) #adds new student to dict
    number += 1 #so that next update doesn't overwrite another student

    index += 3 #"skip" past the @s

print(dict[r.randint(0, len(dict) - 1)])
