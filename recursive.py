from curses import keyname


def rec(fn, arg):
    """Calls given function "fn" on argument "arg" (that is, fn(arg)), and then
    calls fn on the result. That is: "fn(fn(arg)" is returned"""
    return fn(fn(arg))


def mod5(x):
    return x % 5


# lista = [3, 4, 5, 6, 7]
lista = range(30)

print("max(lista):", max(lista))
print("max(lista,key=mod5):", max(lista, key=mod5))
