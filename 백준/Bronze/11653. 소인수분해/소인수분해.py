def PrimeFactorization(num):
    for i in range(2,num+1):
        if num%i==0:
            ans = i
            charge = num//i
            break
    return ans,charge

n = int(input())
while n != 1:
    result,charge = PrimeFactorization(n)
    print(result)
    n = charge
