time = []
for i in range(int(input())):
  start, end = map(int, input().split())
  time.append((start, end))

# 끝 시간 기준으로 먼저 정렬 후, 시작 시간 기준으로 정렬
time = sorted(time, key=lambda x: (x[1], x[0]))

before_end = 0
meeting = 0
for t in time:
  start, end = t[0], t[1]

  if before_end <= start:
    meeting += 1
    before_end = end

print(meeting)
