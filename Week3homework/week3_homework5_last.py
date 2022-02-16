x = ["madam", "tacocat", "utrecht"]
#I created a list where I made the entries.
y = []
#I created an empty list to where ı will add the outputs.
def line():
#I defined a function.    
    for i in x:
#I created a loop and looped an "i" in this loop.      
        if i == i[::-1]:
         y.append(True)
#I added "True" to the y list if i is the same both straight and reverse.
        else:
         y.append(False)
#otherwise, I have appended "False" to the y list.
line()
#I called the function.        
print(y)
#I printed the "y" list. 