# 프로그램 목적 : 파이썬에 대한 기초 이해

# 반드시 알아두어야 할 단축키
# 1. 한 줄 지우기 : ctrl + 'y'
# 2. 실행취소 : ctrl + 'z'
# 3. 한 줄 주석: '#'
# 4. 여러 줄 주석: 블록설정 후 ctrl + '/'
# 5. 처음 실행하는 경우 : ctrl + shift + F10
# 6. 5번 이후에 실행하는 경우 : shift + F10

# 1) 문자열의 출력
print("Hello World")  # 파이썬에서는 문자열에 쌍따옴표(" ")를 붙여 나타낼 수 있다
print('Hello World')  # 파이썬에서는 문자열에 홑따옴표(' ')를 붙여 나타낼 수 있다
# 즉, 파이썬에서는 위 두가지 구문을 혼용하여 쓴다

# 2) 간단한 계산하기
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)
print('2 + 4')  # 따옴표 안에 들어간 수식은 문자열 취급됨에 유의
print(5 / 3)  # 자동으로 묵시적 형변환이 됨 -> 실수 나누기로 인식
print(5 // 3)  # 자동으로 묵시적 형변환이 안 됨 -> 정수 나누기로 인식

# 3) 파이썬은 내부적으로 타입을 가지고 있지만 명시적으로 선언하지는 않음 -> 인터프리터 언어의 특징
print(2345 * 9876 - 5678)
print(123456789123456789 * 123456789123456789)  # C나 C++에서는 오버플로우 발생 -> 파이썬에서는 알아서 형 맞춰줌
print(3.141592 * 10 * 10.0)  # 다른 타입이 있으면 묵시적 형변환이 일어남
print((1/100) * 1234)