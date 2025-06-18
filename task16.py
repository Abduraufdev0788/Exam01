age = int(input("yoshingizni kiriting: "))
price = 100
if age>=0:
    if 0 <= age <= 6 :
        result = price * 0.5
        print(f"Yakuniy narx: {result} so'm (50%chegirma qollanildi)")
    elif 7 <= age <= 17 :
        result = price * 0.8
        print(f"Yakuniy narx: {result} so'm (20%chegirma qollanildi)")
    elif age >= 60 :
        result = price * 0.7
        print(f"Yakuniy narx: {result} so'm (30%chegirma qollanildi)")
    else:
        print("sizga chegirma yo'q")
else:
    print("yoshni togri formatda kiriting: ")