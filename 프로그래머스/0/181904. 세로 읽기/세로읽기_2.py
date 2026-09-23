def solution(my_string, m, c):
    answer = ''
    grid = [] #파이썬은 리스트만 존재해서 리스트를 선언한 것
    
    # my_string을 m개씩 잘라서 2차원 배열에 저장
    for i in range(0, len(my_string), m):
        grid.append(my_string[i:i+m])
    
    # 각 행을 순회하면서 c번째 열 문자를 추출
    for row in grid:
        answer += row[c-1]
        
    return answer
