#try-except 구문을 사용하여 10을 0으로 나누는 코드를 작성하고, 예외 메시지를 출력하시오.

try:
    print(10/0)
except Exception as e:
    print('예외 발생:', e)