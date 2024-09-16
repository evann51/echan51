def big_diff(nums):
  min_num = nums[0]
  max_num = nums[0]
  for num in nums:
    min_num = min(min_num, num)
    max_num = max(max_num, num)
  return max_num - min_num
