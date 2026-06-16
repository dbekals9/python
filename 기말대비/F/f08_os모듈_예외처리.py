#**os 모듈과 예외 처리 결합**  

import os

os.mkdir('exam_folder')

try:
    os.mkdir('exam_folder')
except FileExistsError:
    print('이미 존재합니다.')

os.rmdir('exam_folder')