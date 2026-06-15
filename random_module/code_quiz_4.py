import numpy

from numpy import random

students = ['철수', '영희', '민수', '지은', '수진', '현우']

a = random.choice(students, 3, False)
print(a)