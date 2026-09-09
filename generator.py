# difference between list and tuple
# return and print
# return and yield



'''def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g=mygen()
print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))'''


# Eg 2

def countdown(num):
    print("start Countdown")
    while(num>0):
        yield num
        num=num-1

values=countdown(5)
for x in values:
    print(x)