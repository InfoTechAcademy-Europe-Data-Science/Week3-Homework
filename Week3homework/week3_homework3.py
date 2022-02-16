def siralama(a,b,c,d):
    x = [a, b, c, d]
    x.sort()
    
    return (f"{x[0]}-{x[1]}-{x[2]}-{x[3]}")
a= input("Please enter a color name")
b= input("Please enter another a color name")
c= input("Please enter another a color name")
d= input("Please enter another a color name")

print(siralama(a,b,c,d)) 