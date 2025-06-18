text = input("matn kiriting: ")
unli = "a,e,i,u,o"
count = 0

for i in text.lower():
    if i in unli :
        count += 1
print(f"unli harflar soni {count}")

#unli harflarni kichik harfda yozib textni ham kichik harflarga aylantirib oldim

        