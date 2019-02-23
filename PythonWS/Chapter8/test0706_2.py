# 프로그램 목적: 리스트에 대한 기초실습 2
# 주의) 리스트:[] vs 딕셔너리/셋:{} vs 튜플:()

l1 = ['A', 'B', 'C', 'D', 'E']
print(l1)

# 1) 특정 인덱스의 내용접근
print(l1[0])  # 리스트의 맨 앞 원소츨 출력
print(l1[-1])  # 리스트의 맨 뒤에서 첫 번째 원소 출력
# print(l1[5])  # 리스트의 범위를 벗어난 원소 출력불가
l1[2] = 'X'  # 저장 원소의 값을 변경가능
l1[2] = 'C'  # 저장 원소의 값을 변경가능

# 2) 슬라이싱
print(l1[0:2])  # 0번부터 1번까지 출력 (2번은 제외)
print(l1[2:4])  # 2번부터 3번까지 출력 (4번은 제외)
print(l1[::2])  # A C E 출력
print(l1[0:len(l1):2])  # len()을 통해 리스트의 길이를 알 수 있다

# 3) 리스트의 모든 원소 출력방법
print(l1)
print(l1[::])
for i in l1:  # <=> for i in ['A', 'B', 'C', 'D', 'E']
    print(i, end=' ')
    print(type(i))  # 여기에서는 문자열로 인지되는 점이 다름

# 4) index()의 사용법
print(l1.index('C'))  # 찾고자 하는 값을 넣으면 해당 값의 인덱스를 리턴
print(l1.index('A'))  # 결과값: 0

# 5) sort()의 사용법
l2 = ['A', 'C', 'B', 'c', 'd', 'b', 'a', 'D']
print('정렬되기 전 :', l2)  # ['A', 'C', 'B', 'c', 'd', 'b', 'a', 'D']
l2.sort()  # ASCII 코드에 의거 순서바꿈
print('정렬된 후 :', l2)  # ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']

# 오늘의 문구를 뽑아주는 프로그램
import random as rnd
idiom = ['인생은 그 자체로 소중한 것', '수고했어 오늘도', '나 자신을 사랑하자']
print(rnd.choice(idiom))  # 아무거나 하나 골라줌 -> choice()에 임의의 리스트 넣어도 됨!