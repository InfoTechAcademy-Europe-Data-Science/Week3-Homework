def formule(*numbers):
    unique_list=(set(filter(lambda x:x,numbers)))
    print("Output : ",list(sorted(unique_list)))

formule(100,100,1,2,3,3,3,6,77,77,8,8,9,9,1)
