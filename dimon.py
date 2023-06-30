n=int(input())
for i in range(n//2):
    print(' '*(n//2-i),end='')
    print('*'*(((i+1)*2)-1))
for i in range(n-n//2):
    print(' '*i,end='')
    print('*'*(n-2*i))
    