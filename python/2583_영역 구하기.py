# 백준 2583

from collections import deque

m, n, k = list(map(int, input().split()))

dist = [[0] * n for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()

for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      dist[i][j] = 1

area = []
for i in range(m):
  for j in range(n):
    if dist[i][j] == 0:
      dist[i][j] = 1
      q.append([i, j])
      cnt = 1
      
      while q:  # bfs 탐색
        y, x = q.popleft()
        for k in range(4):
          nx = x + dx[k]          
          ny = y + dy[k]
          if 0 <= ny < m and 0 <= nx < n and dist[ny][nx] == 0:
            dist[ny][nx] = 1
            q.appendleft([ny, nx])
            cnt += 1
      area.append(cnt)

area.sort()
print(len(area))
print(' '.join(map(str, area)))
