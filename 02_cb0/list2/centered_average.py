def centered_average(nums):
  min_num = nums[0]
  min_idx = 0
  max_num = nums[0]
  max_idx = 0
  for i in range(len(nums)):
    if (nums[i] < min_num):
      min_num = nums[i]
      min_idx = i
    elif (nums[i] > max_num):
      max_num = nums[i]
      max_idx = i
      
  total = 0
  total_nums = 0
  for i in range(len(nums)):
    if i == min_idx or i == max_idx:
      continue
    else:
      total += nums[i]
      total_nums += 1
  
  return total / total_nums

