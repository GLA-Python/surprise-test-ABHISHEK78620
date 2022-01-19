def a(number):
    b = ""

    c = number[0]
    number = number[1:]+" "
    d = 1

    for e in number:
        if e != c:
            b += str(d)+c
            d = 1
            repeat = e
        else:
            d += 1

    return b

num = "1"
n = 5

for i in range(n):
    print (num)
    num = a(num)




