#lcm has relation which hcf or gcd

#brute:

a,b=4,8

def lcm(a,b):
  if b>a:
    higher = b
  else:
    higher = a
  value = higher
  while True:
    if higher % a == 0 and higher % b == 0:
      print()
      break
    else:
      higher = higher + value



# best
def gcd(a,b):
  if b==0:
    return b
  else: gcd(b,a%b)



# formula
# lcm(n1 , n2) = (n1 * n2) // gcd(n1 * n2)
lcm = a*b // gcd(a,b)
print(lcm)



