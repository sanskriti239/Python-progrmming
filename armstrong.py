def Armstrong_sanskriti(num):
    n1 = num
    res = 0
    while (n1 != 0):
        rem = n1 % 10
        res = rem ** 3 + res
        n1 = n1 // 10


    if (num == res):
        print( num, "is an armstrong number" )
    else:
        print( num, "is not an armstrong number" )

Armstrong_sanskriti(153)