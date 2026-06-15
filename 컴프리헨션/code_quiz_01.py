# 평균 점수가 70점 이상인 학생만 추출하여 이름과 평균을 딕셔너리로 구성

# 출력 : {'Kim': 89.0, 'Park': 79.0}

students = {
    'Kim': [85, 90, 92],
    'Lee': [60, 65, 70],
    'Park': [75, 80, 82],
    'Choi': [50, 45, 40]
    }

ave = { fn:sum(av)/len(av) for fn, av in students.items() if sum(av)/len(av) >= 70 }

print(ave)