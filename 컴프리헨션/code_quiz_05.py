# 문자열을 입력받아, 각 알파벳 문자의 빈도 수를 딕셔너리로 출력하되,
# 빈도가 2 이상인 문자만 필터링하기(대소문자 구분 안함)

# 입력 : "Hello Python, Hello Code!"
# 출력 예 : {'h':2, 'e': 3, 'l': 4, 'o': 4}

from collections import Counter

sen = input('문장을 입력하세요: ')

# lsen = str.lower(sen)
# cc = dict(Counter(lsen))

x = dict(Counter(str.lower(sen)))
result = { i:j for i, j in x.items() if j >= 2 }
print(result)