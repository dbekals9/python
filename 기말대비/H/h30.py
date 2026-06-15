#os 모듈을 사용하여 "test_folder"를 생성하고, 현재 작업 디렉토리를 출력한 후 폴더를 삭제하는 코드를 작성하시오.

import os
os.mkdir('test_folder')
print(os.getcwd())
os.rmdir('test_folder')