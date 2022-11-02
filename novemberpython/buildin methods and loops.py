
a = 277
b = 33
c = 899
if a > b and c > a:
  print("Both conditions are True")
"""
i = 1
while i < 9:
  print(i)
  i += 1
"""
i = 1
while i < 6:
  print(i)
  if i == 6:
    break
  i += 1



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



list1 = ["Ram", "gopi", "Mohan"]
list2 = [24, 56, 34]
for x, (list1, list2) in enumerate(zip(list1, list2)):
    print(x, list1, list2)