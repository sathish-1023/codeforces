n=int(input())
x=0
y=0
z=0
for i in range(n):
    arr=list(map(int,input().rstrip().split()))
    x+=arr[0]
    y+=arr[1]
    z+=arr[2]
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")
    

    
    
