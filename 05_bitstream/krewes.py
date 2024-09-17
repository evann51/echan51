#Victor Casado
#The Flying Mice
#SoftDev
#K05 -- Processing Bitstreams
#2024-09-17
#time spent: tbd
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
    index += 3

    devo = ""
    while(not (string[index] == '$')):
        devo += string[index]
        index += 1
    index += 3

    ducky = ""
    while(not (string[index] == '@')):
        ducky += string[index]
        index += 1
    index += 3
    dict.update({number: [devo, pd, ducky]})
    number += 1

print(dict[r.randint(0, len(dict) - 1)])
