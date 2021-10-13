n = int(input())
m = int(input())

a1 = []
a2 = []

for i in range(0, n):
    ele = int(input())
 
    a1.append(ele)


for i in range(0, m):
    ele = int(input())
 
    a2.append(ele)

sum1 = 0
sum2 = 0


for i in range(n):
    sum1 += a1[i]

for i in range(m):
    sum2 += a2[i]

if (sum1 % 2 == 0 and sum2 % 2 == 0):
        print(0);
        

if (sum1 %2 == 1)




