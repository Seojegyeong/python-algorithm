def solution(a, b):
    if str(a) + str(b) >= str(b) + str(a):
        return int(str(a) + str(b))
    else:
        return int(str(b) + str(a))
    
    
# = 같은 경우를 고려하지 않아서 틀림
# max로 비교 가능
# def solution(a, b):
#   return max(int(str(a) + str(b)), int(str(b) + str(a)))