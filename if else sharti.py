ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")
    
login = input("Yangi login tanlang:")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart!")   
    
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2022-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2022-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
    
    
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
#ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
#GM uchun ikkala harfni katta qiling.
yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for avto in yangi_cars:
    if avto != 'gm' :
        print(avto.title())
    else:
        print(avto.upper())
        
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
#"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
# xabarini konsolga chiqaring. Aks holda, 
# "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.   
login = input("loginni kiriting:")
if login.lower() == 'admin' :
    print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz {login.title()}!")
    
#Foydalanuvchidan 2 ta son kiritishni so'rang.
# Agar ikki son bir-biriga teng bo'lsa,
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
x = float(input("1-sonni kiriting:"))
y = float(input("2-sonni kiriting:"))
print([f"sonlar teng:{x}={y}" if x==y else f"sonlar teng emas: {x}!= {y} " ])

#2-variant
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")

#Foydalanuvchidan istalgan son kiritishni so'rang. 
#Agar son manfiy bo'lsa konsolga "Manfiy son",
#agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = int(input("Istalgan sonni kiriting:"))
print(["Manfiy son" if son<0 else "Musbat son"])

#2-variant
son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")

#Foydalanuvchidan son kiritishni so'rang, 
#agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
#Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
son = int(input("Istalgan sonni kiriting:"))
print([son**0.5 if son>0 else "Musbat son kiriting"])

#2-variant
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')

