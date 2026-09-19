# Enter the row size for the pattern: 5
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 

rows = 5

for i in range(1,rows + 1):
  for j in range(rows - i):
    print(" ",end=" ")
  for k in range(1, i ):
    print(k,end=" ")
  for j in range(i):
    print(i-j,end=" ")
  print()
