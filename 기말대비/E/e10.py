#파일 "test.txt"에 "Hello Python"을 쓰고 다시 읽어 출력하는 코드를 작성하시오.

file = open('test1.txt', 'w')
file.write('Hello Python')
file = open('test1.txt', 'r')
print(file.read())