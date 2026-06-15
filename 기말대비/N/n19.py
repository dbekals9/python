#try-except-else-finally 구문을 사용하여 문자열 "python"의 10번째 문자를 참조하는 코드를 작성하고, 예외 처리 결과를 출력하시오.

try:
    print('python'[10])
except Exception as e:
    print('예외:', e)
else:
    print('정상')
finally:
    print('종료')