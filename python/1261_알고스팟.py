from collections import deque

m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)] # 가중치
dist[0][0] = 0  # 첫 가중치
q = deque()
dx = [-1, 1, 0, 0]  # 좌우 좌표배열
dy = [0, 0, -1, 1]  # 상하 좌표배열
q.append([0,0])

while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if dist[nx][ny] == -1:
        if maze[nx][ny] == 0:       # (nx, ny)위치의 노드가 0이면
          dist[nx][ny] = dist[x][y] # 이전 가중치 그대로 가져옴
          q.appendleft([nx,ny])     # 큐의 앞부분에 추가
        else: # 1이면
          dist[nx][ny] = dist[x][y] + 1 # 이전 가중치에서 1 증가
          q.append([nx,ny])             # 큐의 마지막에 추가

print(dist[n-1][m-1])
