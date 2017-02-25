n = 1
time = 0

while n < 10000:
    if n % 2 == 1 and n % 3 == 0 and n % 4 == 1 and n % 5 == 1 and n % 6 == 3 and n % 7 == 0 and n % 8 == 1 and n % 9 == 0:
        print(n)
        time += 1
    n += 1

print('\nTotal: ', time)
