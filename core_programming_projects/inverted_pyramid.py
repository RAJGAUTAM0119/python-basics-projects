# Enter the row size for the pattern: 5
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

rows = 5

for i in range(rows):
  for j in range(i):
    print(" ",end=" ")
  for j in range(rows,i,-1):
    print("*",end=" ")
  for j in range(rows-1,i,-1):
    print("*",end=" ")
  print()