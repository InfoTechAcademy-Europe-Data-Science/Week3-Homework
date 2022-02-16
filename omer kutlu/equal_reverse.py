def words(lst):
    cnvrt=[*map(lambda x:x==x[::-1],lst)]
    return print(cnvrt)
a=(input("Enter words with space between whether they are equal to their reversed order or not : ").split(" "))
words(a)