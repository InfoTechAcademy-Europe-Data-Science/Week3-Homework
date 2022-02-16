x=[]

for i in range(1,1001): 
    sayi=0
    for i_2 in range(1, i-1):
        if i % i_2 ==0:
                sayi = sayi+i_2    
        
    if sayi == i:
        x.append(i)
        #print(i)

y = []
for i in range(1,1001):
    y.append(i)
new_list = list(filter(lambda i: i in x, y))
print(new_list)