n = int(input())
cnt = 0


for i in range(n+1):
  for j in range(60):
    for k in range(60):
      #if (k%10)==3 or (k//10)==3 or (j%10)==3 or (j//10)==3 or (i%10)==3:
      if '3' in str(i)+str(j)+str(k):
        cnt += 1

print(cnt)