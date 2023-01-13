multiply = lambda var1, var2: var1*var2
print(multiply(5,6))


temp = 56

print("value of temp before function", temp)

def test():
    global temp
    temp=9
    print(" value of temp inside",temp )

test()
print(" value now ", temp)







