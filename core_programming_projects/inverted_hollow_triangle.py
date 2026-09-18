# Enter the row size for the pattern: 4
# * * * * 
# *   * 
# * * 
# * 

rows = 20

for i in range(rows):
  for j in range(rows,i,-1):
    if (j == rows or i == 0 or j - i == 1):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()