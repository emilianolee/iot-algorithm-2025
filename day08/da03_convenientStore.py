import random

# 클래스와 함수 선언
def binSearch(ary, data):
    start = 0
    end = len(ary) - 1

    while start <= end: 
        mid = (start + end) // 2
        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1 
        else:
            end = mid - 1
    
    return - 1

# 전역 변수 선언
dataAry = ['바나나맛우유','레쓰비캔커피','츄파춥스','도시락','삼다수','코카콜라','삼각김밥']