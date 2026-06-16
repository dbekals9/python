#**모듈과 패키지 활용**  

import os
os.mkdir('기말대비/F/myai')
os.mkdir('기말대비/F/myai/ml')

with open('기말대비/F/myai/ml/machine.py', mode='w') as file:
    file.write('''
def getML():
    print("I'm ML Module")
    ''')

from myai.ml import machine
machine.getML()

os.remove('기말대비/F/myai/ml/machine.py')
os.remove('기말대비/F/myai/ml/__pycache__/machine.cpython-314.pyc')
os.rmdir('기말대비/F/myai/ml/__pycache__')
os.rmdir('기말대비/F/myai/ml')
os.rmdir('기말대비/F/myai')