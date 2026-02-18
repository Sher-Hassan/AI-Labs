import random
def genFun():
    return list(random.randint(1, 100) for _ in range(5))

print(genFun())