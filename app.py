#1
docs = input("Hujjat topshirdingizmi? (ha/yo'q): ").lower()
interview = input("Suhbatdan o'tdingizmi? (ha/yo'q): ").lower()
test = input("Testdan o'tdingizmi? (ha/yo'q): ").lower()

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")

elif docs == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")

elif docs == "ha" and interview == "yo'q":
    print("Suhbatdan o'tmagansiz.")

elif docs == "ha" and interview == "ha" and test == "yo'q":
    print("Test natijalari yetarli emas.")

else:
    print("Jarayon davom etmoqda.")


#2
sentence = input("Jumla kiriting: ")

words = sentence.split()
secret = "" 

for w in words:
    secret += w[0]

print(secret)

#3
royxat = [4, 7, 2, 5, 1, 10]
yangi = [i * royxat[i] for i in range(len(royxat))]
print(yangi)


#4
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

# So'zlarni uzunligi bo'yicha tartiblash (eng uzunlari birinchi)
sorted_words = sorted(words, key=len, reverse=True)

first_longest = sorted_words[0]
second_longest = sorted_words[1]

print("1-chi eng uzun so'z:", first_longest)
print("2-chi eng uzun so'z:", second_longest)
