
def caching_fibonacci():
    cashe = {}

    def fibonacci(n):
        if not n in cashe:
            if n == 0:
                cashe[n] = 0
            elif n <= 2:
                cashe[n] = 1
            else:
                cashe[n] = fibonacci(n-2)+fibonacci(n-1)
            return cashe[n]
        else:
            return cashe[n]
    return fibonacci


a = caching_fibonacci()
print(a(8))
