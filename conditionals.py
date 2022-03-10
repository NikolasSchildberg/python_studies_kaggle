def inspect(x):
    if x == 0:
        return print(x,"is zero")
    elif x > 0:
        return print(x,"is positive")
    elif x < 0:
        return print(x,"is negative")
    else:
        return print(x,"it is unlike anything I have ever seen")

inspect(0)
inspect(10)
inspect(-10)