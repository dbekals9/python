#with open("data.txt", "w") as f: 구문을 사용하여 "Python File Test"를 파일에 쓰고, 다시 읽어 출력하시오.

with open('data.txt', 'w') as f:
    f.write('Python File Test')

with open('data.txt', 'r') as f:
    print(f.read())