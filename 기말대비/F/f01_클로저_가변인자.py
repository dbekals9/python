#**클로저와 가변 인자 결합**  

def make_inc(n):
    def func(*args):
        return sum(args) + n
    return func

inc10 = make_inc(10)
print(inc10(1,2,3))