# 입력한 문장에서 길이가 4자 이상인 단어만 대문자로 변환한 리스트 출력

# 입력 : "The quick brown fox jumps over the lazy dog"
# 출력 : ['QUICK', 'BROWN', 'JUMPS', 'OVER', 'LAZY']

sen = input("문장을 입력하세요: ")
words = sen.split()

#1

print([w for w in map(str.upper, filter(lambda x: len(x) >= 4, words))])


#2
'''
result = map(str.upper, filter(lambda x: len(x) >= 4, words))
print([w for w in result])
'''

#3
'''
def long(word):
    return len(word) >= 4

filtered = filter(long, words)
mapped = map(str.upper, filtered)
result1 = [w for w in mapped]
print(result1)
'''