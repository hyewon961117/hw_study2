def calc_func(a, b):
    x = a
    y = b
    
    def plus():
        p = x +y
        return p
    
    def minus():
        m = x-y
        return m
    return plus, minus

print(calc_func(10,20))