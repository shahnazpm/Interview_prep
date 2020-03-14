# maximum reduced string by removing the repeats

def maxreducedString(S):
  LS = list(S)
  i = 0
  while i < len(LS) - 1:
    if LS[i] == LS[i + 1]:
      del LS[i]
      #print LS[i]
      del LS[i]
      # i = 0
      if len(LS) == 0:
        print('Empty String')
        break
    else:
      i += 1
  return ''.join(LS)


print(maxreducedString('aaabccddd'))