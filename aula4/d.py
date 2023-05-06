n, m = map(int, input().split())
status = list(map(int, input().split()))
room_control = [[] for _ in range(n+1)]
adj = [[] for _ in range(m)]
 
color = [-1] * m
 
visited = [False] * m
 
def bfs(u, visited):
	color[u] = 0
	q = [u]
	h = 0
	visited[u] = True
	
	while (h<len(q)):
		u = q[h]
		h+=1
		for v in adj[u]:
			if (color[v[0]] == -1):
				color[v[0]] = color[u]^v[1]
				q.append(v[0])
				visited[v[0]] = True
			else:
				if color[v[0]] != color[u]^v[1]: return False
	return True
 
for i in range(m):
	b = list(map(int, input().split()))
	for j in range(1, len(b)):
		k = b[j]
		room_control[k].append(i)
		if len(room_control[k])==2:
			adj[room_control[k][0]].append((room_control[k][1],1-status[k-1]))
			adj[room_control[k][1]].append((room_control[k][0],1-status[k-1]))
			
possible = True
for i in range(m):
	if color[i] == -1:
		if bfs(i, visited) == False:
			possible = False
			break
 
if possible: print("YES")
else: print("NO")