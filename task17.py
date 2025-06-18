ball = int(input("bal kiriitng (0-100) : "))

if 0 <= ball <= 100:
    if 90 <= ball <=100 :
        print("A (A'lo)")
    elif 80 <= ball <=89 :
        print("B (Yaxshi)")
    elif 70 <= ball <=79 :
        print("C (Qoniqarli)")
    elif 60 <= ball <=69 :
        print("D (Qoniqarsiz)")
    else:
        print("F (Rad)")
else:
    print("(0-100) oraliqda qiymat kiriting")