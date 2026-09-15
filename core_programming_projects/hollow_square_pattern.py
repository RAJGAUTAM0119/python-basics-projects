# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

rows = 5


for i in range(rows):
  for j in range(rows):
    if( 0 < i < rows - 1 and 0 < j < rows - 1 ):
      print(" ", end=" ")
    else:
      print("*", end=" ")
  print()