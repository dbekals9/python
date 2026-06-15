#**kwargs를 사용하여 이름, 나이, 주소를 출력하는 함수를 작성하시오.

def func(**kwargs):
    for i, j in kwargs.items():
        print(i,':',j)

func(이름='홍길동', 나이=30, 주소='서울')