"""strs = "Month Python"
#         01234567891011 (프로그래밍에서는 항상 숫자는 0부터 시작, 띄어쓰기 포함)

# slicing (슬라이싱) : 문자열을 슬라이스한다 (자른다)
print (strs[6:10]) # [a : b] : a부터 b-1번째의 문자열을 출력한다
print (strs[:10]) # [:a] : 처음부터 a-1번째의 문자열을 출력한다
print (strs[4:]) # [a:] : n번째까지의 문자열이 있다면 a번째부터 마지막번째의 문자열을 출력한다
"""

# slicing 연습하기

str = "abcdefghijklmnopqrstuvwxyz"
#      01234567890123456789012345

print (str[1:2]) # b만 출력될 거임

print (str[:2]) # a b

print (str[1:]) # a 빼고 전부 다 출력

print (str[0:]) # 전부 다 출력

print (str[0] + str[15] * 2 + str[11] + str[4]) # apple 출력