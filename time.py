# 시간 제어 모듈 time
import time

# 1. time() : 1970년 1월 1일 0시 0분 0초부터 현재까지의 시간을 초 단위로 반환   
# print(time.time())
# 2. localtime() : 현재 시간을 년, 월, 일, 시, 분, 초 등의 형태로 반환
# print(time.localtime())
# print("현재 시간:", time.localtime().tm_year, "년", time.localtime().tm_mon, "월", time.localtime().tm_mday, "일",
#       time.localtime().tm_hour, "시", time.localtime().tm_min, "분", time.localtime().tm_sec, "초")
# 3. strftime() : 시간을 문자열로 포맷팅
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 4. sleep() : 일정 시간 동안 프로그램을 일시 정지
# print("3초 동안 대기...")
# time.sleep(3)
# print("3초가 지났습니다.")

# [팁] 시간 차이 계산
start_time = time.time()  # 시작 시간 기록
# 예시: 1초 동안 대기
print("1초 동안 대기...")
time.sleep(1)
end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산
print("경과 시간:", elapsed_time, "초")