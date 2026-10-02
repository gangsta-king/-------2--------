#  ( ax + b ) : ( cx + d ) = 0.
# a,b,c,d = int(input()),int(input()),int(input()),int(input())
# if a==0 and b==0:
#     print('INF')
# elif a==0 or b % a != 0:
#     print('NO')
# else:
#     x = -b // a
#     if c * x + d == 0:
#         print('NO')
#     else:
#         print(x)

# a,b,c,d = int(input()),int(input()),int(input()),int(input())
# print(((c*100+d)-(a*100+b))//100,((c*100+d)-(a*100+b))%100)

# k = int(input())
# if k == 1 or k == 2 or k == 4 or k == 7:
#     print('NO')
# else:
#     print('YES')

# k,m,n = int(input()),int(input()),int(input())
# if n==0:
#     print(0)
# elif n<=k:
#     print(2*m)
# else:
#     print((2*n+k-1)//k*m)

# x,y,x1,y1= int(input()),int(input()),int(input()),int(input())
# if x*x1 > 0 and y*y1 > 0:
#     print('YES')
# else:
#     print('NO')
    
# print(max(int(input()),int(input())))

a,b,c = int(input()),int(input()),int(input())
if a+b>c and a+c>b and b+c>a:
    print('YES')
else:
    print('NO')