import random
import string

print("welcome to our Random Password Generator")

def pswrd():
    while True:
       length = int(input("Enter the length of password you want(8-32): "))
       if length and 8 <= int(length) <= 32:
           length = int(length)
           break
       else:
           print("Invalid input. Please enter a number between 8 and 32")
           
    while True:
        char = input("Enter the character you want((l)owercase, (u)ppercase, (d)igits, (s)ymbols e.g:lud))")
        char = char.lower()
        if set(char).issubset({'l','u','d','s'}):
            break
        else:
            print("Invalid input. Please enter")
            
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolsD = string.punctuation
    combine = lowerD + upperD + digitD + symbolsD
    if not combine:
        print("Invalid input. Please enter atleast one valid character")
        pswrd()
        return
    
    x = random.sample(combine,length)
    password = "".join(x)
    print(password)
    pswrd()
pswrd()