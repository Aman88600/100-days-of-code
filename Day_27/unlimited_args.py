# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i

#     return sum

# print(add(1,1,1,1))

def calculate(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])

calculate(a=1)