def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Can't posible divide to zero"
    return a / b

if __name__ == "__main__":
    print(add(5, 3))
    print(sub(5, 3))
    print(mult(5, 3))   
    print(div(5, 3))
    print(div(5, 0))
