def array_front9(nums):
  x = 4
  if(len(nums)<4):
    x= len(nums)
  for i in nums[0:x]:
    if(i == 9):
      return True
  return False
