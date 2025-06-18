letter = input("harf kiriting: ")

if letter.isalpha() and len(letter)==1:
    if letter.isupper :
        print("Katta harf")
    else:
        print("kichik harf")
else:
    print("togri qiymat kiriting: ")
