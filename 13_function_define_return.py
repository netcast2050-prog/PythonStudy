# 함수 생성
def total__values(input_value):
    # 지역 변수 선언
    total = 0

    # 입력값이 리스트인 경우
    if isinstance(input_value, list):
        for i in input_value:
            total += i

    # 입력값이 딕셔너리인 경우
    elif isinstance(input_value, dict):
        for key in input_value:
            total += input_value[key]

    # 결과 반환
    return total

def process_data(data):

    # 숫자 리스트인 경우
    if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
        return sum(data)

    # 문자 리스트인 경우
    elif isinstance(data, list) and all(isinstance(x, str) for x in data):
        return "".join(data)

    # 딕셔너리인 경우
    elif isinstance(data, dict):
        return sum(data.values())

    # 그 외
    else:
        return "지원하지 않는 타입입니다."


# 함수 호출
# print(total__values([1, 2, 3, 4, 5]))
# print(total__values({'a': 1, 'b': 2, 'c': 3}))

# print(process_data([1, 2, 3, 4, 5])) 
# # 15

# print(process_data({"a": 10, "b": 20, "c": 30}))  
# # 60

# print(process_data(["안녕", "하세요", "!"]))
# # 안녕하세요!

print(process_data([1, 2, '3', '4', '5']))
# 지원하지 않는 타입입니다.
