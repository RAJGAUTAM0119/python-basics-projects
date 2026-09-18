# Enter the row size for the pattern: 5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

row = 5

for i in range(row):
  for j in range(row-1,i,-1):
    print(" ",end=" ")
  for k in range(i+1):
    print("*",end=" ")
  for k in range(i):
    print("*",end=" ")
  print()