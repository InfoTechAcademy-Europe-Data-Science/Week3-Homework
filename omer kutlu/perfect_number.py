from functools import reduce
def pn(x):    
    top=0  
    for i in range(1,x):
        if x%i==0:
            top+=i
            if top==x:
                return x

numbers=int(input("Sum Of Perfect Numbers Between 1 to 'x'? ---> Enter 'x' :"))
print("Sum Of Perfect Numbers ----> ",reduce(lambda x,y:x+y,(filter(pn,list(range(1,numbers+1))))))