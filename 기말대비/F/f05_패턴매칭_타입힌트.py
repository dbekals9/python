#**패턴 매칭과 타입 힌트 결합**  

def process(data:list[int]) -> str:
    match data:
        case []:
            return 'Empty'
        case [0, *re]:
            return 'Zero Start'
        case _:
            return 'Valid'

print(process([]))
print(process([0, 1]))
print(process([2, 3]))