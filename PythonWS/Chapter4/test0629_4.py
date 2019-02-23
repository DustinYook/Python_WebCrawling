# 프로그램 목적 : 문자열에 대한 실습 -> 시험 100% 출제 (출력결과 예측)
string = '0123456789'  # 문자열은 문자상수들의 배열
print(string)

# 1-1) 특정 인덱스에 있는 원소 출력 -> 양수
print(string[0])
print(string[3])

# 1-2) 특정 인덱스에 있는 원소 출력 -> 음수
# 앞에서 셀 때는 '0'부터 세고, 뒤부터 셀 때는 '-1'부터 셈
# 참고) C 언어와 다르게 파이썬은 뒤에서부터 셀 때 음수를 붙임
print(string[-1])  # 뒤에서부터 1번째 있는 원소 -> 9
print(string[-3])  # 뒤에서부터 3번째 있는 원소 -> 7

# 2) 범위지정 원소출력 -> 반드시 연습 많이 해보기!
# string[시작 인덱스:끝 인덱스:간격]
# 시작 인덱스 디폴트 값 (생략 시) -> 0번 인덱스
# 끝 인덱스 디폴트 값 (생략 시) -> 마지막 인덱스
# 간격 디폴트 값 (생략 시) -> 1칸
print(string[1:5])  # 앞에서부터 1번부터 5번까지 출력 -> 1234
print(string[-4:-1])  # 뒤에서부터 4칸 앞으로 와서 뒤에서부터 1번까지 출력 -> 678
print(string[-4:0])  # 주의) 출력방향은 왼쪽에서 오른쪽 -> 아무것도 출력 안 됨!
print(string[-4:])  # 뒤에서 4개 앞으로 와서 끝까지 출력한다는 의미!
print(string[1:8:2])  # 1부터 8까지 2칸씩 건너뛰면서 뽑음
print(string[1:8:3])  # 1부터 8까지 3칸씩 건너뛰면서 뽑음
print(string[1::2])  # 1부터 끝까지 2칸씩 건너뛰면서 뽑음
print(string[::2])  # 첫번째부터 끝까지 2칸씩 건너뛰면서 뽑음
print(string[5::])  # 마지막 생략하면 건너뛰는 간격이 1로 함
print(string[::])  # 0번부터 마지막까지 건너뛰는 간격이 1로 함

# 3) 문자열의 길이 출력
print('문자열의 길이는 ', len(string), ' 입니다.', sep='')
substring = string[::2]  # 시작부터 끝까지 2칸씩 건너뛴 부분문자열 -> 02468
print('부분문자열은 ', substring, '입니다.', sep='')
print('부분문자열의 길이는 ', len(substring), ' 입니다.', sep='')