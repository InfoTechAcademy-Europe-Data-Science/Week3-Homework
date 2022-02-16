def two_digit_number(x):
    second_num = int(x // 10)
    firs_num = int(x % 10)
   
    
    a = {1:"ten", 2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    b = {1:"one", 2:"two", 3: "üç",4:"dört", 5:"beş", 6:"altı",7:"yedi",8:"sekiz",9:"dokuz",0:""}
    return f" {x}------------>{a[second_num]} {b[firs_num]} "

number = int(input("Please enter two digit number"))
print(two_digit_number(number))
