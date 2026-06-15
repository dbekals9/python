cart = ["apple", "banana", "apple", "orange", "banana", "apple"]

scart = set(cart)

counts = {}

for i in cart:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
        
market = tuple(counts.items())

print(market)
print(type(market))