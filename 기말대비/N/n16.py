#구조적 패턴 매칭을 사용하여 상태 코드 404가 들어왔을 때 "Not Found"를 출력하는 코드를 작성하시오.

status = 404
match status:
    case 200: print('OK')
    case 400: print('Bad Request')
    case 404: print('Not Found')
    case _: print('Something is Wrong..!')