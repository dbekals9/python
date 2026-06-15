a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

inter = set(a) & set(b)
print(inter)

z = zip(a, b)

sums = []

for c, d in z:
    sums.append(c+d)
print(sums)

print(list(enumerate(sums)))