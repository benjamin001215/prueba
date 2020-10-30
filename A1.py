n = int(input())
while n<1 or n>100:
    n = int(input())
ones = 0
for i in range(n):
    n = int(input())
    if n == 1:
        ones += 1
if ones > 0:
    print('HARD')
else:
    print('EASY')