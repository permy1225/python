# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import sys

dial = []
firstLoop = True
for l in sys.stdin:
  if firstLoop:
    rule = list(map(int,l.split()))
    firstLoop = False
    continue
  dial.append(int(l))
key_number = rule[0]
keys = list(range(key_number))
num_of_dials = rule[1]
border = rule[2]
position = keys[0]
result = 'Yes'

for dial in dial:
  amount_of_move = dial-position
  if 0 < amount_of_move < key_number/2:
    border -= amount_of_move
  elif 0 > amount_of_move:
    border -= abs(amount_of_move)
  else:
    border -= (key_number-amount_of_move)
  if border < 0:
    result = 'No'
    break
  position = keys[dial]

print(result)