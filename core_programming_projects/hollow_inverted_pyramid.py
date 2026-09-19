# Enter the row size for the pattern: 5
# * * * * * * * * * 
#   *           * 
#     *       * 
#       *   * 
#         * 

rows = 10

for i in range(1,rows + 1):
  for j in range(1,i):
    print(" ",end=" ")
  for k in range( 2 * rows , 2 * i - 1, -1):
    if k == 2 * rows or i == 1 or k == 2 * i :
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()