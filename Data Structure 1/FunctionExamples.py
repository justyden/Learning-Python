def Sum(list1):
    total = 0
    for i in list1:
        total += i
    return total


list1 = [1, 3, 5, 6, 10, 15, 29, 34, 45]
list2 = []

print(Sum(list1))


def RecSum(list1):
    if len(list1) == 0:
        return 0
    elif len(list1) == 1:
        return list1[0]
    else:
        return list1[0] + RecSum(list1[1:])


print(RecSum(list1))


def Fact(inputNum):
    if inputNum == 1 or 0:
        return 1
    else:
        return inputNum * Fact(inputNum - 1)


print(Fact(6))


def Fibo(inputNum):
    if inputNum == 0:
        return 0
    elif inputNum == 1:
        return 1
    else:
        return Fibo(inputNum - 2) + Fibo(inputNum - 1)


def FiboA(inputNum):
    a = 0
    b = 1

    for i in range(inputNum):
        a, b = b, a + b

    return a


print(Fibo(11))
print(FiboA(11))
