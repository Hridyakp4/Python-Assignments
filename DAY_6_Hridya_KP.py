def div(a, b):
    return a // b

def modified_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        func(a, b)
    return inner

a, b = (int(i) for i in input("Enter two values: ").split())
print(div(a, b))