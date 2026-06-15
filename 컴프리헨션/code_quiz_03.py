# 좌표 리스트에서 모든 좌표를 x축 기준으로 좌우대칭 이동시키는 리스트 생성
# (x좌표만 부호 반전)

# 출력 : [(-3, 4), (2, 5), (-6, -7), (0, 0)]

coords = [(3, 4), (-2, 5), (6, -7), (0, 0)]
cdict = dict(coords)
rev = { i * -1:j for i, j in cdict.items() }
clist = list(map(lambda x: (x[0], x[1]), rev.items()))

print(clist)