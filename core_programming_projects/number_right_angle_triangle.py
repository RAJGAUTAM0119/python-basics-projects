# Enter the row size for the pattern: 4
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 

rows = 5

for i in range(1,rows + 1):
  for j in range(1,i+1):
    print(j,end=" ")
  print()


# Enter the row size for the pattern: 5
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

rows = 5

for i in range(1,rows+1):
  for j in range(1,rows + 2 - i):
    print(j,end=" ")
  print()