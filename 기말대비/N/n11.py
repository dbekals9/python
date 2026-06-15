#클로저를 활용하여 기준값 100을 더하는 함수를 생성하고, inc100(10)을 호출하여 결과를 출력하시오.

def inc(n):
    def add(x):
        return n + x
    return add

inc100 = inc(100)
print(inc100(10))