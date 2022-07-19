def funrec(n):
    print('inicial', n)
    if n == 1:
        return 1
    else:
        n=n+funrec(n-1)
        print('final', n)
        return  n
        
n = 5
print(funrec(n))
