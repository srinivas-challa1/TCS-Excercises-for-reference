def check_prime(number):
    flag = -1
    for i in range(2, number//2):
        if(number % i == 0):
            flag = 0
            break
        else:
            flag = 1
    return(flag)


def prime_composite_list(numlist):
    p = []
    c = []
    res = []
    for num in numlist:
        if(check_prime(num) == 1):
            p.append(num)
        elif(check_prime(num) == 0):
            c.append(num)
    res.append(p)
    res.append(c)
    return(res)


if __name__ == "__main__":
    count = int(input())
    numlist = []
    for _ in range(count):
        numlist.append(int(input()))
    print(prime_composite_list(numlist))
