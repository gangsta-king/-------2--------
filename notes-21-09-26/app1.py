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

# a,b,c = int(input()),int(input()),int(input())
# if a+b>c and a+c>b and b+c>a:
#     print('YES')
# else:
#     print('NO')

# n=int(input())
# c=0
# for i in range(n):
#     s=input()
#     if s.startswith('Set') and s.endswith('answer'):
#         if len(s[3:-6]) >c:
#             c=len(s[3:-6])
# print(c)

# n = int(input())
# v = 0  # Счётчик подходящих чисел x

# # Перебираем нечётные числа x от 1 до n
# for x in range(1, n + 1, 2):
#     # 1. Считаем количество делителей числа x
#     c = 0
#     for j in range(1, x + 1):
#         if x % j == 0:
#             c += 1
            
#     # 2. Проверяем, является ли количество делителей (c) нечётным и простым
#     if c > 2 and c % 2 != 0:
#         # Проверяем c на простоту
#         s = 0
#         for j in range(1, c + 1):
#             if c % j == 0:
#                 s += 1
#         # Если у количества делителей c ровно 2 делителя (1 и c), то c — простое
#         if s == 2:
#             v += 1

# print(v)

n = int(input())
n=n%7
match n:
    case 0:
        print('Monday')
    case 1:
        print('Tuesday')
    case 2:
        print('Wednesday')
    case 3:
        print('Thursday')
    case 4:
        print('Friday')
    case 5:
        print('Saturday')
    case 6:
        print('Sunday')