davlatlar = ["O'zbekiston", "Tojikiston", "Qirg'iziston", "Qozog'iston", "Turkmaniston"]
print(davlatlar)
print(len(davlatlar))
print("sorted=",sorted(davlatlar))
print("sorted,reverse =True",sorted(davlatlar,reverse = True))
print("Asl ro'yxat = ",davlatlar)

davlatlar.reverse()
print("asil ro'yxat reversev=", davlatlar)

davlatlar.sort()
print("sort metodi=", davlatlar)

davlatlar.sort(reverse=True)
print("alifboga teskari=", davlatlar)

print("120dan 1200gacha bo'lgan toq sonlar ro'xati = ",
      [x for x in range(120,1200) if x%2 ])
print("120dan 1200gacha bo'lgan juft sonlar ro'xati = ",
      [x+1 for x in range(120,1200) if x%2 ])

sonlar = list(range(120,1200))
print("Ro'yxatdagi sonlar yig'indisini xisoblash = ",sum(sonlar))
     
print("Ro'yxatdagi eng katta va eng kichik sonlar ayirmasi = ",
      max(sonlar)-min(sonlar))

print("Royxatdagi elementlar soni=",len(sonlar))

print("Ro'yxatni boshidan 20ta qiymat=", sonlar[:20])
print("o'rtasidan=", sonlar[530:550])
print("oxiridan=", sonlar[-20:])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = []
taomlar.append('butterbrod')
taomlar.append('gamburger')
taomlar.append('xoddog')
taomlar.append('osh')
taomlar.append('shorva,choy')
print(taomlar)

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta =taomlar[:]
print(nonushta)

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring,
# va qo'shimcha 2 ta taom qo'shing. Ikkala ro'yxatni ham 
#(taomlar va nonushta) konsolga chiqaring
nonushta.remove("osh")
nonushta.append('qaymoq')
nonushta.append('sumalak')
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring
nonushta = tuple(nonushta)
print(nonushta)
nonushta =list(nonushta)
nonushta[0] = 'murabbo'
print(nonushta) 

