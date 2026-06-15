# 1부터 100 사이의 수 중에서 소수만 생성하는 제너레이터를 작성하고
# 이를 이용해 소수의 합을 구하기

# 소수 판별 함수와 함께 제너레이터 컴프리헨션 사용

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = (x for x in range(1, 101) if prime(x))

print(f"소수들의 합: {sum(primes)}")
