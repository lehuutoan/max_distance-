def maxdistance(s):
   n = input()
   if n == ' ':
       return []
   else:
    ham = []
    khoangcach = 0
    for i in range(len(s)):
      if s[i] == n:
        ham.append(i)
    if len(ham) >= 2:
        khoangcach = ham[len(ham)-1] - ham[0]
    else: 
        khoangcach = []
    return khoangcach

s = str(input())
print(maxdistance(s))

  
