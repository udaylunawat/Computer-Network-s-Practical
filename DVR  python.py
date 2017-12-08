
import numpy as np
d= np.zeros((10,10))
via = np.zeros((10,10))
g = np.zeros((10,10))
n= input("\nEnter the no of nodes :")
n= int(n)
i= 0
int(i)
j=0
int(j)

for i in range(n):
  print("Enter the record for route %c "% (i+97))
  for j in range(n):
    print("%c : %c :: " % (i+97,j+97),end='')
    g[i][j]= int(input())
    if g[i][j]!=99:
      d[i][j]=1

for i in range(n):
  for j in range(n):
    via[i][j]= i;

for i in range(n):
  for j in range(n):
    if d[i][j]==1:
      for k in range(n):
        if g[i][j] + g[j][k] < g[i][k]:
          g[i][k] = g[i][j] + g[j][k]
          via[i][k] = j
        
for i in range(n):
  print("Cost of route %c : "% (i+97))
  for j in range(n):
    print("%c : %d via %c "% (int(j+97), g[i][j], int(via[i][j]+ 97)));




     
  


