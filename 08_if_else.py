# # 조건문 if 
# age = 20
# if age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")

# # 조건문 if-elif-else
# score = 85
# if score >= 90:
#     print("학점: A")
# elif score >= 80:
#     print("학점: B")
# else:
#     print("학점: C")

# # 중첩 조건문
# age = 20
# if age >= 18:
#     if age >= 65:
#         print("노인입니다.")
#     else:
#         print("성인입니다.")
# else:
#     print("미성년자입니다.")

# # 조건 표현식 (삼항 연산자)
# age = 20
# message = "성인입니다." if age >= 18 else "미성년자입니다."
# print(message)  # 성인입니다.

# message = "노인입니다." if age >= 65 else ("성인입니다." if age >= 18 else "미성년자입니다.")
# print(message)  # 성인입니다.

# [팁] 조건 표현식은 간단한 조건문을 한 줄로 작성할 때 유용하지만, 복잡한 조건문에는 가독성이 떨어질 수 있으므로 주의해서 사용해야 합니다.  
# message = (
#     "노인입니다." if age >= 65 
#     else
#         "성인입니다." if age >= 18 
#         else "미성년자입니다."
# )
# print(message)  # 성인입니다.

# if 문 작성
age = 20
# if age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")

# if age >= 65:
#     print("노인입니다.")
# else:
#     print("성인입니다.")

# 중첩 if 문 작성
# if age >= 18:
#     if age >= 65:
#         print("노인입니다.")
#     else:
#         print("성인입니다.")
# else:
#     print("미성년자입니다.")

# if 문에 논리 연산자 사용
# if age >= 18 and age < 65:
#     if age >= 65:
#         print("노인입니다.")
#     else:
#         print("성인입니다.")
# else:
#     print("미성년자입니다.")

# else if 문 작성
# if age >= 65:
#     print("노인입니다.")
# elif age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")

# 전자 키트에서 버튼 값을 읽어와서 조건문으로 처리하는 예시
# button_pressed = True  # 버튼이 눌렸다고 가정
# if button_pressed:
#     print("버튼이 눌렸습니다.")
# else:
#     print("버튼이 눌리지 않았습니다.")

# 전자 키트에서 3개의 버튼 값을 읽어와서 조건문으로 처리하는 예시
button1_pressed = False
button2_pressed = False
button3_pressed = True

if button1_pressed:
    print("버튼 1이 눌렸습니다.")
if button2_pressed:
    print("버튼 2가 눌렸습니다.")
if button3_pressed:
    print("버튼 3이 눌렸습니다.")