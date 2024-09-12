def string_match(a, b):
  l = 0
  c = 0
  r = 0
  if(len(a)<2 or len(b)<2):
    return 0
  if(len(a)>len(b)):
    l = len(b)
  else:
    l = len(a)
  for x in a[0:l-1]:
    if(b[c]==x):
      if(b[c+1]==a[c+1]):
        r+=1
    c+=1
  return r