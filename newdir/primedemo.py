def printPrime(start, end):
    l = list()
    for num in range(start, end):
        for x in range(2, num):
            if num % x == 0:
                break
        else:
            l.append(num)
    return l


def writeIntoFile(filename, l):
    with open(filename, "w") as fh:
        fh.write(str(l))


writeIntoFile("result.txt", printPrime(1, 300))
