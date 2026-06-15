names = ["Tom", "Jane", "Mike", "Sara"]
scores = [80, 95, 70, 90]

dic_1 = zip(names, scores)

sum = 0

for a in scores:
    sum += a
ave = sum/len(scores)

dic_2 = {}

for name, score in zip(names, scores):
    if score > ave:
        dic_2[name] = score
        
print(ave)
print(dic_2)