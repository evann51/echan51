def sum67(nums):
  total = 0
  found6 = False
  for i in range(len(nums)):
    if nums[i] == 6:
      found6 = True
    else:
      if found6:
        if nums[i] == 7:
          found6 = False
      else:
        total += nums[i]
  return total

