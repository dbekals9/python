#딕셔너리 컴프리헨션을 사용하여 문자열 리스트 ["apple", "banana", "cherry"]의 첫 글자를 키로, 단어를 값으로 가지는 딕셔너리를 생성하시오.

words = ['apple', 'banana', 'cherry']
dc = {i:i[0] for i in words}
print(dc)