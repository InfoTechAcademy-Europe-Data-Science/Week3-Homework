zero_to_nineteen=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
"Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
two_digits=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
def zero_19(digit):
    if 0<digit<20:
        print(zero_to_nineteen[digit])
        return""
    elif 0!=digit>=20:
        a=0
        b=0
        a=int(digit/10)
        b=int(digit%10)
        print(two_digits[a]+" "+zero_to_nineteen[b])
        return""
enter_digit=int(input("Please Enter a Number Between 1-99 :"))
print(zero_19(enter_digit))
