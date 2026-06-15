#*args를 사용하여 임의 개수의 숫자를 받아 합을 출력하는 함수를 작성하시오.

def sumNumber(*args):
    print(sum(args))

sumNumber(1, 2, 3, 4)