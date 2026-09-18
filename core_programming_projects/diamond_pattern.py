# Enter the row size for the pattern: 4
#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

rows = 5

for i in range(rows):
  for j in range(rows-1,i,-1):
    print(" ",end=" ")

  # without inner two extra loop
  # print(" *" * i,end=" ")
  # print("* " * (i + 1),end=" ")
  
  
  for j in range(i+1):
    print("*",end=" ")
  for j in range(i):
    print("*",end=" ")
  
  print()
  
for i in range(rows-1):
  for j in range(i+1):
    print(" ",end=" ")

  # without inner two extra loop
  # print(" *" *( rows - i - 1),end=" ")
  # print("* " * (rows - i - 2 ),end=" ")
  
  # with inner two extra loop
  for j in range(rows,i+1,-1):
    print("*",end=" ")
  for j in range(rows-2,i,-1):
    print("*",end=" ")  
    
  print()