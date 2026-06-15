#기본값 매개변수를 가진 함수 greet(name, message="안녕!")를 작성하고, 인자를 하나만 전달했을 때와 두 개를 전달했을 때의 결과를 출력하시오.

def greet(name, message='안녕!'):
    print(name, message)

greet('Alex') #인자 하나만 전달
greet('Jhon', 'Hi!') #인자 두 개 전달