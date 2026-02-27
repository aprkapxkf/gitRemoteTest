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

# 리스트 : 일련의 값이 모인 집합을 다루는 자료형. 순서가 있고 내용을 변경할 수 있음.
# '[]' 대괄호로 감싸서 표현하고, 각 요소의 자료형은 무엇이든 될 수 있으며 서로 섞여도 무관.
fruits = ['오렌지', '사과', '배', '바나나']
list_empty = list()
print(list_empty)
list_hello = list('hello')
print(list_hello)
rainbow_split = "빨-주-노-초-파-남-보".split('-')
print(rainbow_split)
print(fruits)
# 인덱싱은 특청 위치의 값을 추출
print(fruits[0])
print(fruits[-1])
# 슬라이싱 : 특정 범위의 값 추출 [시작 : 끝 : 간격]
numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[2:5])
print(numbers[:4])
야차클럽1 = ['조용환', '이성호']
야차클럽2 = ['전현우', '이영훈']
print(야차클럽1+야차클럽2)
a= [10,20,30]
b = a
a.append(40)
print(len(b))

# 튜플 : 리스트와 유사하게 일련의 값이 모인 집합을 다루기위한 자료형으로 **순서**가 있음. 하지만 한번 할당 된 내용들을 변경할 수 없습니다.
# () 소괄호를 사용하거나 괄호 없이 , 를 사용. 데이터의 안정성이 보장됩니다.

tp1 = 1,2,3
print(tp1)
tuples1 = (1,2,3,4,5),(6,7,8,9)
print(f"전체튜플 : {tuples1}")
print(f"첫 번째 요소 : {tuples1[0]}")
print(f"중첩요소 : {tuples1[0][2]}")

#튜플 수정 시도
test_tp = (1,2,3)
#test_tp[0] = 100 # 오류가 난다
print(f"재할당 후 주소 : {id(test_tp)}")
print(test_tp)
test_tp = (4,5,6)
print(f"재할당 후 주소 : {id(test_tp)}")
print(test_tp)