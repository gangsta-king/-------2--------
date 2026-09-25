# print('Hello \nWorld!')

# a = 45 #integer int 
# b = 4.5 #decimal float
# c='hello' #text string str
# print(type(a),type(b), type(c))

# import math
# print(math.ceil(4.3)) #rounds up
# print(math.floor(4.7)) #rounds down
# print(math.sqrt(36)) #square root
# print(math.pow(2,3)) #power
# print(math.pi) #pi
# print(math.e) #e
# print(math.sin(math.pi/2)) #sine
# print(math.cos(math.pi)) #cosine
# print(math.tan(math.pi/4)) #tangent
# print(math.log(100,10)) #logarithm base 10
# print(math.log(100)) #natural logarithm
# print(math.factorial(5)) #factorial
# print(math.gcd(12, 15)) #greatest common divisor
# print(math.lcm(12, 15)) #least common multiple
# print(math.isqrt(16)) #integer square root
# print(math.degrees(math.pi/2)) #convert radians to degrees
# print(math.radians(90)) #convert degrees to radians
# print(math.hypot(3, 4)) #hypotenuse
# print(math.dist((1, 2), (4, 6))) #distance between two points
# print(math.comb(5, 2)) #combinations
# print(math.perm(5, 2)) #permutations
# print(math.prod([1, 2, 3, 4])) #product of a list
# print(math.fsum([0.1, 0.2, 0.3])) #accurate floating point sum
# print(math.isclose(0.1 + 0.2, 0.3)) #check if two numbers are close
# print(math.copysign(1, -5)) #copy sign
# print(math.frexp(8)) #mantissa and exponent
# print(math.ldexp(0.5, 3)) #multiply by power of two
# print(math.modf(3.14)) #fractional and integer parts
# print(math.nextafter(1.0, 2.0)) #next floating point number
# print(math.ulp(1.0)) #unit in the last place
# print(math.remainder(5, 3)) #remainder
# print(math.trunc(3.9)) #truncate
# print(math.fmod(5, 3)) #floating point modulus
# print(math.exp(1)) #e raised to the power of 1
# print(math.expm1(1)) #e raised to the power of 1 minus 1
# print(math.log1p(1)) #natural logarithm of 1 plus x
# print(math.log2(8)) #logarithm base 2
# print(math.log10(100)) #logarithm base 10
# print(math.isfinite(1.0)) #check if number is finite
# print(math.isinf(float('inf'))) #check if number is infinite
# print(math.isnan(float('nan'))) #check if number is NaN
# print(math.copysign(1, -5)) #copy sign
# print(math.fabs(-5)) #absolute value
# print(math.factorial(5)) #factorial
# print(math.gamma(5)) #gamma function
# print(math.lgamma(5)) #log gamma function
# print(math.erf(1)) #error function
# print(math.erfc(1)) #complementary error function
# print(math.isclose(0.1 + 0.2, 0.3)) #check if two numbers are close
# print(math.isqrt(16)) #integer square root
# print(math.prod([1, 2, 3, 4])) #product of a list


# import random
# print(random.random()) # 0 - 1
# print(random.randint(100)) # 0 - 100 integer

# minutes=int(input())
# print(f'{minutes//60} hours, {minutes%60} minutes')

# n=4567
# nfirst=n%10
# nsecond=(n//10)%10
# nthird=(n//100)%10
# nlast=(n//1000)%10

# n,m,k = int(input()),int(input()),int(input())
# if k//m > n:
#     print('Yes')

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [i[1:] for i in keywords]

# print(new_keywords)

# palindromes = [[f'{i}{j}{i}' for j in range(0,10)] for i in range(1,10)]

# for i in palindromes:
#     print(*[int(j) for j in i])

# palindromes = [int(f'{i}{j}{i}') for i in range(1,10) for j in range(0,10)]

# print(*palindromes)

# print(*[i**2 for i in list(map(int,input().split())) if i%2==0 and int(str(i**2)[-1]) != 4])

# алгоритм пузырьковой сортировки
# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

# n = len(a)

# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print(a)


# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)

# k=a
# l=[]

# for i in range(len(a)):
#     c=min(k)
#     l.append(c)
#     del k[k.index(min(k))]

# print(l)

#  Алгоритм сортировки — это алгоритм упорядочивания элементов в списке. Алгоритмы сортировки оцениваются по скорости выполнения и эффективности использования памяти:

# время — основной параметр, характеризующий быстродействие алгоритма;
# память — ряд алгоритмов требует выделения дополнительной памяти под временное хранение данных.
# ✅ Основные алгоритмы сортировки:

# Медленные:
# Пузырьковая сортировка (Bubble sort)
# Сортировка выбором (Selection sort)
# Сортировка простыми вставками (Insertion sort)
# Быстрые:
# Сортировка Шелла (Shell sort)
# Быстрая сортировка (Quick sort)
# Сортировка слиянием (Merge sort)
# Пирамидальная сортировка (Heap sort)
# Сортировка TimSort (используется в Java и Python)
# Не основанные на сравнениях:
# Сортировка подсчетом (Counting sort)
# Блочная сортировка (Bucket sort)
# Поразрядная сортировка (Radix sort)

# n=input().split()
# print(max(list(len(i) for i in n)))

# a,b,n=int(input()),int(input()),int(input())
# if (n%b==0 and n//b < a) or (n%a==0 and n//a < b):
#     print('YES')
# else:
#     print('NO')

# v,n=int(input()),int(input())
# print(v*n % 109)

# print((int(input())//2+1)*2)

# n=int(input())
# print((n+2)-(n%2))

# n=3606 # seconds
# minut = (n // 60) % 60
# hours = (n // 3600) % 24
# sec = n % 60

# print(f'{hours//10}{hours%10}:{minut//10}{minut%10}:{sec//10}{sec%10}')

n=int(input())
lesson=n*45
odd = 5
even= 15
