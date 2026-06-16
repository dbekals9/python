#**파일 입출력과 pickle 결합**  

import pickle

arg = [{'name':'Alice', 'score':90}, {'name':'Bob', 'score':80}]

with open('students.pic', 'wb') as file:
    pickle.dump(arg, file)

with open('students.pic', 'rb') as file:
    data = pickle.load(file)

for d in data:
    print(d['name'], d['score'])