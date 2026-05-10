# 반복문 for in range pass continue break
# for i in range(1, 11):
#     if i == 5:
#         pass
#     print(i)
# print('반복문 종료')
# for i in range(1, 11):
#     if i >= 5 and i <= 8:
#         continue
#     print(i)
# print('반복문 종료')
# for i in range(1, 11):
#     if i >= 5:
#         break
#     print(i)
# print('반복문 종료')

while True:
    num = int(input('숫자를 입력하세요: '))
    if num < 0:
        print('음수는 입력할 수 없습니다. 다시 입력하세요.')
        continue
    elif num == 0:
        break     
    print(f'입력한 숫자는 {num}입니다.')
print('프로그램 종료')