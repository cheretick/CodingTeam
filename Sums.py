
def rangeSum(n,m):
    result = 0
    for i in range(n,m+1):
        result += i
    return result

n, m = eval(input("Enter two numbers: "))
print("The sum of", n, "though", m, "is", rangeSum(n,m))

def rangeSum2(n,m):
   return int(((m*(m+1))/2)-((n*(n+1))/2) + 1)

print("The sum of", n, "though", m, "is", rangeSum2(n,m))