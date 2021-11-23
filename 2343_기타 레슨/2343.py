# 백준 2343

n, m = map(int, input().split())  # n = 강의의 수, m = 블루레이의 수
lesson = list(map(int, input().split()))

high = sum(lesson)  # 모든 강의를 더한 값
low = max(lesson)   # 강의 중 길이가 가장 긴 강의

while low <= high:
  sum = 0
  blu_ray = 0
  mid = (low + high) // 2       # 임의로 정한 블루레이 크기

  for i in range(n):
    if sum + lesson[i] > mid:   # mid보다 커지면
      sum = 0
      blu_ray += 1              # 블루레이 개수 1 증가
    sum += lesson[i]            # 첫 번째 강의부터 하나씩 더함

  if sum:   # mid보다 작아서 블루레이 개수를 증가시키지 못 한 경우
    blu_ray += 1

  if blu_ray <= m:
    high = mid - 1    # 블루레이의 크기 감소
  else:  # blu_ray > m
    low = mid + 1     # 블루레이의 크기 증가
    
print(low)
