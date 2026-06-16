#**제너레이터와 예외 처리 결합**  

def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()

try:
    while True:
        print(next(g))
except StopIteration:
    print('내용없음')