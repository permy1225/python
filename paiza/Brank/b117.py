import sys

global num_of_car
count = 0
order = []
firstLoop = True
for line in sys.stdin:
  if firstLoop:
    num_of_car = int(line)
    firstLoop = False
    continue
  order.append(int(line))
sorted_order = sorted(order)
for i in range(num_of_car-1):
  while sorted_order != order:
    for j in range(0, num_of_car-1-i):
      if order[j] > order[j+1]:
        order[j], order[j+1] = order[j+1], order[j]
    count += 1
print(count)
