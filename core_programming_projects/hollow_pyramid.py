# Enter the row size for the pattern: 5
#         * 
#       *   * 
#     *       * 
#   *           * 
# * * * * * * * * * 

rows = 5

for i in range(1,rows+1):
  for j in range(rows - i):
    print(" ",end=" ")

  
  for k in range(1,2 * i):
    if k == 1  or k == 2 * i - 1 or i == rows:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()