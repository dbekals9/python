#제너레이터 컴프리헨션을 사용하여 1부터 10까지 제곱수를 생성하고, next()로 하나씩 출력하시오.

z = (n**2 for n in range(1, 11))

for i in range(10):
    print(next(z), end=' ')