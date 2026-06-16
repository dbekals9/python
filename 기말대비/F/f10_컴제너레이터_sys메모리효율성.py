#**컴프리헨션과 제너레이터 메모리 효율성 비교**  

import sys

lst = [x for x in range(1000000)]
gen = (x for x in range(1000000))

print('리스트메모리: ', sys.getsizeof(lst))
print('제너레이터메모리: ', sys.getsizeof(gen))