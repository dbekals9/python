#filter() 함수를 사용하여 리스트 [-3, -1, 0, 2, 4]에서 양수만 추출하여 출력하시오.

lst = [-3, -1, 0, 2, 4]

def func(x):
    return x > 0

print(list(filter(func, lst)))