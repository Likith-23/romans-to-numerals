def romantoint(romaninput):
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    result = 0 
    for i in range(0, len(romaninput)-1):
        if roman[romaninput[i]]<roman[romaninput[i+1]]:
            result -= roman[romaninput[i]]
        else:
            result += roman[romaninput[i]]
    return result + roman[romaninput[-1]]
roman1 = input("INPUT A ROMAN NUMERAL")
print("INTEGER VALUE", romantoint(roman1))