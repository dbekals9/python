#기본 인자로 리스트를 사용하는 함수에서 발생하는 문제를 obj=None으로 해결하는 코드를 작성하시오.

def func(a, obj=None):
    if obj is None:
        obj = []
    obj.append(a)
    return obj

print(func(1))
print(func(2))