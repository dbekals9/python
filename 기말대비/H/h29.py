#pickle 모듈을 사용하여 숫자 10을 "data.pic" 파일에 저장하고 다시 읽어 출력하시오.

import pickle
file = open('data.pic', 'wb')
pickle.dump(10, file)
file = open('data.pic', 'rb')
print(pickle.load(file))