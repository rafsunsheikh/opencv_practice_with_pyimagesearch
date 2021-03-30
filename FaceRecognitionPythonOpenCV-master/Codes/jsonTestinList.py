import json

score = [1,2,3,4,5]

with open("file.json","w") as f:
    json.dump(score,f,indent=2)

with open("file.json", "r") as f:
    score1 = json.load(f)

print(score1)