def array123(nums):
  c = 0
  found = False
  if(len(nums)<3):
    return False
  for x in nums[0:len(nums)-2]:
    if(x==1):
      if(nums[c+1]==2 and nums[c+2]==3):
        found=True
    c+=1
  return found