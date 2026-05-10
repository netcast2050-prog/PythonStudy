# 반복문 for in range
# range() 함수는 지정된 범위의 숫자를 생성한다.
# for 변수 in range(시작, 끝, 증가치):
# for i in range(5):
#     print(i)
# # 0부터 4까지 출력한다.
# # range(시작, 끝) 형태로 사용하면 시작부터 끝-1까지의 숫자를 생성한다.
# for i in range(1, 6):
#     print(i)
# # 1부터 5까지 출력한다.
# # range(시작, 끝, 증가치) 형태로 사용하면 시작부터 끝-1까지의 숫자를 증가치만큼 생성한다.
# for i in range(0, 10, 2):
#     print(i)
# 0부터 9까지 2씩 증가시키면서 출력한다.
# 중첩 반복문과 range() 함수를 사용하여 구구단을 출력할 수 있다.
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()  # 각 단마다 줄바꿈을 추가한다.
# 2단부터 9단까지 구구단을 출력한다.
