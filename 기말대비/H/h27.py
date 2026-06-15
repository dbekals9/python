#타입 힌트에서 Callable[[float, float], float]을 매개변수로 받아 두 수를 더하거나 곱하는 함수를 실행하는 코드를 작성하시오.

from typing import Callable
def addmul(func:Callable[[float, float], float], a:float, b:float) -> float:
    return func(a, b)

print(addmul(lambda x, y: x + y, 3, 5))
print(addmul(lambda x, y: x * y, 3, 5))