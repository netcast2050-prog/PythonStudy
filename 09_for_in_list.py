# 반복문 for in 리스트
# 리스트의 요소를 하나씩 꺼내서 변수에 저장하고, 반복문을 실행한다.
# # for 변수 in 리스트:
# texts = ['사과', '배', '복숭아', '딸기', '포도']
# for text in texts:
#     print(text)

# # str도 반복문으로 사용할 수 있다.
# for char in 'Hello':
#     print(char)

# 중첩 리스트(Nested List = 2차원 리스트)
# 2차원 리스트는 리스트 안에 리스트가 있는 형태이다.
# nested_list = [['사과', 2000], ['배', 3000], ['복숭아', 4000]]
# for item in nested_list:
#     print(item)
#     for element in item:
#         print(element)

# 리스트 컴프리헨션(List Comprehension)
# 리스트 컴프리헨션은 기존 리스트를 기반으로 새로운 리스트를 만드는 방법이다.
# 기존 리스트에서 짝수만 뽑아서 새로운 리스트를 만들어보자.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
# 기존 리스트에서 각 요소에 2를 곱해서 새로운 리스트를 만들어보자.
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)
# 기존 리스트에서 각 요소를 문자열로 변환해서 새로운 리스트를 만들어보자.
string_numbers = [str(num) for num in numbers]
print(string_numbers)
# 중첩 리스트에서 각 요소의 첫 번째 요소만 뽑아서 새로운 리스트를 만들어보자.
nested_list = [['사과', 2000], ['배', 3000], ['복숭아', 4000]]
first_elements = [item[0] for item in nested_list]
print(first_elements)