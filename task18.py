height = float(input("bo'yingizni uzunligini kiriting: "))
vazn = int(input("vazningizni kiriting: "))

if height >0 and vazn > 0 and 0.5 <= height <= 3.0 and 1 <= vazn <= 500:
    BMI = vazn / (height*height)
    if BMI < 18.5:
        print("Kam Vazn")
    elif 18.5 <= BMI < 25:
        print("normal vazn")
    elif 25<= BMI < 30 :
        print("ortiqcha vazn")
    else:
        print("semizlik")
        
#hamma shartlar toliq bajarildi