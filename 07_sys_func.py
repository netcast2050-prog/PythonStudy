# 시스템 관련 모듈
import os
import sys

# os
# print(os.name)
# print(os.getcwd())
# print(os.listdir())
# sys
# print(sys.version)
# print(sys.platform)

# 터미널에서 입력한 인지 값 사용하기
# 실행 시 입력한 값이 리스트 형태로 저장됨
# 예 > python sys_func.py 홍길동 100 1524 실행
# print(sys.argv) # ['sys_func.py', '홍길동', '100', '1524']
name = sys.argv[1]
age = sys.argv[2]
bath = sys.argv[3]
print(f'이름: {name}, 나이: {age}, 탄생년도: {bath}')