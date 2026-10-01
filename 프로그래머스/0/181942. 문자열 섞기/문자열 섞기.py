def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer

# 인덱스로 직접 순회하는 방식 
# 두 문자열의 길이가 같으니까 len만큼 answer는 i번째 합쳐서 출력하기