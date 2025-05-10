def sumrange(value):
    if value==0:
        return 0
    return value+sumrange(value-1)

print(sumrange(5))