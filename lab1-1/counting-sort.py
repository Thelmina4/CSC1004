#!/usr/bin/env python3

# s/i = seq of numbers, terminated w "end"
#       can't use sel sort
# s/o = that line sort

times = [0] * 999
nums = [0] * 999
s = input()

while s != "end":
   nums[int(s)] = int(s)
   times[int(s)] += 1
   s = input()
#print(times)
#print(nums)
i = 0
while i < len(nums):
   if times[i] > 0:
      number = (str(nums[i]) + "\n") * times[i]
      print(number.rstrip())
   i += 1
