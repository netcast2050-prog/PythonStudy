# 반복문 while input() : 사용자로부터 입력을 받는 함수

basket = []
while True:
    item = input("장바구니에 담을 물건을 입력하세요 (종료하려면 '0' 입력): ")
    if item == '0':
        break
    basket.append(item)

print(f"장바구니에 담긴 물건들: {basket}")