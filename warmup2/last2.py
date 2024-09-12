def last2(str):
  counter = -1
  if len(str)<2: return 0
  for i in range(len(str)-1):
    if(str[i:i+2]==str[len(str)-2:]):
      counter+=1
  return counter
