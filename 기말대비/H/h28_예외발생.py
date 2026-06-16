#raise Exception("양의 정수를 입력하시오")를 사용하여 음수 입력 시 예외를 발생시키는 코드를 작성하시오.

n = -1
if n <= 0:
    raise Exception('양의 정수를 입력하시오')