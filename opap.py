from itertools import combinations
import string
import requests
import json
from collections import Counter



draw_id = int(input("Enter Draw ID: "))
num = int(input("Enter Range: "))
combinationRange = int(input("Enter Combination Range: "))
numList = {}
for x in range(1,81):
    numList[x] = 0




for i in range(0,num):
    a=requests.get(f"https://api.opap.gr/draws/v3.0/1100/{draw_id}")       
    b=json.loads(a.content)
    for w in range(0,20):
        numList[b["winningNumbers"]["list"][w]] += 1
    draw_id = draw_id - 1


sort_numList = sorted(numList.items(), key=lambda x: x[1], reverse=True)

top10 = []
for i in range(0,10):
    top10.append(sort_numList[i][0])

combinationList = []
tempList = []

draw_id = draw_id - combinationRange
for i in range(0,combinationRange):
    a=requests.get(f"https://api.opap.gr/draws/v3.0/1100/{draw_id}")       
    b=json.loads(a.content)
    for i in top10:
        if i in b["winningNumbers"]["list"]:
            tempList.append(i)
    combinationList.append(tempList)
    tempList = []
    draw_id = draw_id + 1




for i in combinationList:
    print(i)
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")

for i in sort_numList:
	print(f"{i[0]} showed up {i[1]} times")

input("Press enter to exit ;)")
