#**고급 함수 인자 활용**  

def example(a, b=2, *args, c, d=5, **kwargs):
    print(f'a: {a}\nb: {b}\nargs: {args}\nc: {c}\nd: {d}\nkwargs: {kwargs}')

example(10, 20, 30, 40, c=50, e=60, f=70)