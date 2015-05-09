sum1 = 0
sum2 = 0

for i in range(1,101):
    sum1+=i*i
    sum2+=i
    print(i)
print(str(sum2 * sum2 - sum1))