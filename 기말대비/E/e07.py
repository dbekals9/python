#map() 함수를 사용하여 리스트 [1, 2, 3, 4]의 각 원소를 두 배로 만든 결과를 출력하시오.

lst = [1, 2, 3, 4]

def func(x):
    return x*2

print(list(map(func, lst)))