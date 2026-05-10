# 랜덤과 난수 관련 모듈
import random
# # random() : 0.0 ~ 1.0 사이의 난수 반환
# print(random.random())
# # randint(a, b) : a 이상 b 이하의 정수 난수 반환
# print(random.randint(1, 255))
# # randrange(a, b) : a 이상 b 미만의 정수 난수 반환
# print(random.randrange(1, 255))
# # uniform(a, b) : a 이상 b 이하의 실수 난수 반환
# print(random.uniform(1.0, 10.0))

# 리스트와 랜덤
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# choice() : 리스트에서 랜덤하게 하나의 요소 반환
print(random.choice(numbers))
# sample() : 리스트에서 랜덤하게 지정된 개수의 요소 반환
print(random.sample(numbers, 3))
# shuffle() : 리스트의 요소를 랜덤하게 섞음
random.shuffle(numbers)
print(numbers)