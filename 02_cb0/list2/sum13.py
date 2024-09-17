def sum13(nums):
  total = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      if i < len(nums) - 1:
        nums[i+1] = 0
    else:
      total += nums[i]
  return total

