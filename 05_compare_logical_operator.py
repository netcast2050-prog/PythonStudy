# 비교 연산자
# 비교 연산자는 두 값을 비교하여 참(True) 또는 거짓(False)을 반환하는 연산자입니다.
# 주요 비교 연산자:
# == : 두 값이 같으면 참(True), 그렇지 않으면 거짓(False)
equal = (5 == 5)  # True
not_equal = (5 != 3)  # True
less_than = (5 < 10)  # True
greater_than = (5 > 10)  # False
less_than_equal = (5 <= 5)  # True
greater_than_equal = (5 >= 5)  # True

# 논리 연산자
# 논리 연산자는 여러 조건을 결합하여 참(True) 또는 거짓(False)을 반환하는 연산자입니다.
# 주요 논리 연산자: and, or, not
# and: 두 조건이 모두 참일 때 참(True), 그렇지 않으면 거짓(False)
and_result = (5 > 3) and (10 > 5)  # True
# or: 두 조건 중 하나라도 참일 때 참(True), 그렇지 않으면 거짓(False)
or_result = (5 > 3) or (10 < 5)  # True
# not: 조건의 반대 값을 반환합니다.
not_result = not (5 == 3)  # True