#**딕셔너리 컴프리헨션과 zip 활용**  

subjects, scores = ['math', 'english', 'science'], [90, 85, 70]

dct = {i:j for i, j in zip(subjects, scores)}
print(dct)