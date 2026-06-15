import random

items = ["볼펜", "노트", "이어폰"]

print(random.choices(items, 
weights=[0.7, 0.2, 0.1], k=10))