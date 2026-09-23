def solution(n, slicer, num_list):
    
    a, b, c = slicer #언패팅으로 가독성 확보
    
    if n == 1:
        return num_list[0:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 4:
        return num_list[a:b+1:c]

# slice(시작, 끝, 간격)