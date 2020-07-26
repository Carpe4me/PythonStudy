# capitalize    : 첫 문자를 대문자로 변환
# count         : 문자열의 개수를 반환
# startwith     : 문자열이 특정 문자로 시작하면 참
# endwith       : 문자열이 특정 문자로 끝나면 참
# find          : 찾을 문자열의 첫 번째 인덱스를 반환, 실패시 -1
# index         : find와 같은 역활, 실패시 ValueError 반환
# isalpha       : 모든 문자가 알파면 참.
# isdecimal     : 모든 문자가 숫자면 참
# isalnum       : 모든 문자가 알파나 숫자면 참
# lower         : 소문자로 변환
# upper         : 대문자로 변환
# replace       : 문자열의 문자를 다른 문자료 교체
# strip         : 문자열의 맨 앞과 맨뒤의 빈 칸을 제거
# split         : 구분자를 지정하여 문자열을 나누고, 나눈 값들의 리스트를 반환
# partition     : split 과 동일 역활 수행, 구분자도 반환
# center        : 지정한 너비로 문자열을 늘이고 문자열을 가운데 정렬
# zfill         : 문자열의 빈 칸을 '0'으로 채운다.

word = 'grail'
sent = 'a scratch'

print(word[0])
print(sent[0])

print(word[0:3])

# 09-3 문자열 포매팅
var = 'flesh wound'
s = "It's just a {}!"

print(s.format(var))
print(s.format('scratch'))