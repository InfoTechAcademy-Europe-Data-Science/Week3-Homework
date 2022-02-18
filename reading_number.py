def reading_number():
    birler =[",","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    onlar =[",","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    number = int(input("2 Basamaklı bir sayı giriniz:"))
    s =str(number)
    print(onlar[int(s[0])],birler[int(s[1])])
reading_number()





