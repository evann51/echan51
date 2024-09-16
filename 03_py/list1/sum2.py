def sum2(nums):
  sum=0
  if(len(nums)<2):
    for x in nums:
      sum+=x
  else:
    return nums[0]+nums[1]
  return sum
