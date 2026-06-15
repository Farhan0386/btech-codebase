def recursion(n):
    if n==0 or n==1:
        return n
    else:
        res = n*recursion(n-1)
        return res  
result = recursion(5)
print(result)