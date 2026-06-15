#기본 인자로 리스트를 사용하는 함수에서 연속 호출 시 값이 누적되는 문제를 보여주는 코드를 작성하시오.

def func(a, l = []):
    l.append(a)
    return l

print(func(1))
print(func(2))