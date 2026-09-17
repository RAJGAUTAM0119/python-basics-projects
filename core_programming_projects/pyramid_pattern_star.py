rows = 5

for i in range(rows):
  for j in range(i+1):
    print("* ",end=" ")
  print('\r')
  
for i in range(rows):
  for k in range(rows -1,i, -1):
    print("* ",end=" ")
  print('\r')

  # without inner loop triangle shape pattern
  # print("* " *( i + 1),end=" ")
  # print()