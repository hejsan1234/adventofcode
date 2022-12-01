with open('rasmus.txt') as f:
  lines = f.readlines()
  def addArr(arr):
    print(arr)
    man = 0;
    max = 0;
    currentMax = 0;
    for e in arr:
      if (e != ''):
        currentMax += int(e);
      else:
        if (currentMax > max):
          max = currentMax;
        elif(currentMax < max):
          currentMax = 0;
          continue
        man += 1
        currentMax = 0;
    return max, man

  arr = ['4601\n', '1583\n', '\n', '1583\n', '1583\n']
  new = []
  test = 0
  for e in lines:
    new.append(e.replace("\n", ""))

  result = addArr(new)
  print(result)