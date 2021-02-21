import re

p = re.compile("ca.e")
def print_match(m):
    if m:
        print("m.group : " , m.group()) # 일치하는 문자열 반환
        print("m.string : " , m.string) # 입력받은 문자열
        print("m.start() : " , m.start()) # 일치하는 문자열의 시작
        print("m.end() : " , m.end())  #일치하는 문자열의 끝
        print("m.span() : " , m.span()) #일치하는 문자열의 시작/끝
    else:
        print("x")

m = p.search("good care")
print_match(m)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") - 주어진 문자열의 처음부터 일치하는지
# 3. m = p.search("비교할 문자열") - 주어진 문자열 중에 일치하는게 있는지
# 4. lst = p.findall("비교할 문자열") - 일차흐는 모든 것을 리스트로 변환

# https://www.w3schools.com/python/python_regex.asp