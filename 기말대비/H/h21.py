#클로저를 활용하여 입력값을 n만큼 증가시키는 함수 생성기를 작성하고, inc5(10) → 15, inc10(10) → 20을 출력하시오.

def inc(n):
    def num(x):
        return x + n
    return num

inc5 = inc(5)
inc10 = inc(10)
print(inc5(10)) #n = 5, x = 10
print(inc10(10)) #n = 10, x = 10