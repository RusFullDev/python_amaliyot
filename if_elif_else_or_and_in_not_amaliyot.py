#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son 
#kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" 
#degan xabarni chiqaring.

son = int(input("Juft son kiriting:"))
print([f"Bu {son}-soni juft  emas" if son%2 else "Raxmat!"]) #1-usul

if son%2:                             #2-usul
    print("Bu son juft emas")
else:
    print("Raxmat")

#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini 
#quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh = int(input("Yoshingiz nechida?:"))
if 60 < yosh or 4 > yosh :
    price = 0
elif yosh < 18 :
    price = 10000
else:
    price = 20000
print(f" Chipta narxi {price} so'm")

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va 
#ularning teng yoki katta/kichikligi haqida xabarni chiqaring
son1 = float(input("1-sonni kiriting>>>"))
son2 =float(input("2-sonni kiriting>>>>"))
if son1 == son2 :
    print(f"{son1}={son2}")
elif son1 > son2 :
    print(f"{son1}>{son2}")
else:
    print(f"{son1}<{son2}")
    
    
#Maxsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
#Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga
#kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni,
#mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa
#"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan
#xabarlarni chiqaring.

maxsulotlar = ["un", "yog'", "kartoshka", "olma", "banan", "shakar", "uzum",
               "sabzi", "makkaron", "choy", "tuxum","tuz", "shokolad"]
savat = []
print("5 xil maxsulotni kiriting")
for maxsulot in range(5):
   savat.append(input(f"{maxsulot+1}-maxsulot:\t"))

if savat:
    for maxsulot in savat:
        if maxsulot in maxsulotlar:
           print(f"Do'konimizad {maxsulot} bor")  
        else:
            print(f"Do'konimizda {maxsulot} yoq")

#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot
 #kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang,
# bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa 
 #mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
# aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan 
# xabarni chiqaring.
maxsulotlar = ["un", "yog'", "kartoshka", "olma", "banan", "shakar", "uzum",
               "sabzi", "makkaron", "choy", "tuxum","tuz", "shokolad"]  
bor_mahsulotlar = []
mavjud_emas = []    
savat = []
print("5 xil maxsulotni kiriting")
for maxsulot in range(5):
   savat.append(input(f"{maxsulot+1}-maxsulot:\t"))

if savat:
    for maxsulot in savat:
        if maxsulot in maxsulotlar:
           bor_mahsulotlar.append(maxsulot)  
        else:
            mavjud_emas.append(maxsulot)
if mavjud_emas :
    print("Do'konimizda quyidagi maxsulotlar yoq:")
    for maxsulot in mavjud_emas:
        print(maxsulot)   
else:
    print("Siz so'ragan barcha maxsulot do'konimizda bor")
    
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
#Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
#loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
#Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, 
#yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" 
# xabarini chiqaring.

users = ['ilxom', 'abror', 'nodir', 'olim', 'orif']
login = input("Yangi loging tanlang:\t")

if login.lower() in users :
    print("Login band,boshqa login tanlang !")
else:
    print(f"Xush kelibsiz,{login}")
    
#Foydalanuvchidan biror butun son kiritishni so'rang.
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga 
# qoldiqsiz bo'linishini konsolga chiqaring.
son = int(input("istalgan sonni kiriting:\t"))
for i in range(2,11):
    if not(son%i) :
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")
        
    

            
        
    

 