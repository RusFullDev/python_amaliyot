ismlar = ["Ilxom", "Nodir", "Olim", "Salim", "G'ofur", "Ilyos"]
for ism in ismlar:
    print(f"Salom {ism.upper()} ishlaringiz yaxshimi")

print(f"Kod {len(ismlar)} marta takrorlanadi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)
    
    
sonlar =[x**3 for x in range(10,100) if x%2]
print(f"10dan 100gacha bo'lgan toq sonlar kubi:{sonlar}")

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta sevimli kinongizni yozing")
for k in range(5):
    kinolar.append(input(f"{k+1}- kino\t:"))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing.
# Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun nechta kishi bilan suxbat qildingiz?\n"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1} -suxbat qilgan odamingiz kim edi?"))
print(ismlar)