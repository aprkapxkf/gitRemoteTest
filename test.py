print("10")
# 정수(int) : 소수점이 없는 숫자
num1 = 10
num2 = -5
print(num1)
print(num2)
print(num1,type(num2))

print("더하기 : ", num1+num2)

money = 50
person = 3

# 활용도가 높은 연산자
print("몫 : ", money//person)
print("나머지 : ", money % person)
print("거듭제곱 : ", money ** person)

# 정수와 실수의 혼합 연산은 항상 결과가 실수이다.
# 파이썬은 연쇄 비교가 가능함
age = 25
print("10 <= age <= 30", 10 <= age <= 30)
# 문자열 비교 : 사전 순 비교
print("apple < banana", 'apple' < 'banana')
print("apple > banana", 'apple' > 'banana')
# 주의 : 문자열 vs 숫자 비교
print("'10' < '9'", '10' < '9')
print("'python' < 'Python'", 'python' < 'Python')

poem = """안녕하세요 우린 매직 서커스유랑단
님찾아 꿈을찾아 떠나간다우
동네집 계집아이 함께 간다면
천리만길 발자욱에 꽃이 피리라"""
print(poem)
greeting = " 우리는 크라잉넛 떠돌이신사"
print(poem+greeting)
text1 = "    헬로  파이썬    "
print(text1.strip())
simple_str = "Python"
print(dir(simple_str)) # dir 함수는 자료형이 가진 모든 기능을 리스트로 보여줌
print(help(simple_str.upper)) # help : 특정 기능의 사용법을 가르쳐줌

# 리스트 : 일련의 값이 모인 집합을 다루는 자료형. 순서가 있고 내용을 변경할 수 있음.
# '[]' 대괄호로 감싸서 표현하고, 각 요소의 자료형은 무엇이든 될 수 있으며 서로 섞여도 무관.
fruits = ['오렌지', '사과', '배', '바나나']
list_empty = list()
print(list_empty)
list_hello = list('hello')
print(list_hello)