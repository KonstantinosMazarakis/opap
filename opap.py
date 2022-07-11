from click import prompt
import requests
import json
from collections import Counter



draw_id = int(input("Enter Draw ID: "))
num = int(input("Enter Range: "))
numList = {}
for x in range(1,81):
    numList[x] = 0




for i in range(1,num):
    a=requests.get(f"https://api.opap.gr/draws/v3.0/1100/{draw_id}")       
    b=json.loads(a.content)
    for w in range(0,20):
        numList[b["winningNumbers"]["list"][w]] += 1
    draw_id = draw_id - 1


sort_numList = sorted(numList.items(), key=lambda x: x[1], reverse=True)

for i in sort_numList:
	print(f"{i[0]} showed up {i[1]} times")


