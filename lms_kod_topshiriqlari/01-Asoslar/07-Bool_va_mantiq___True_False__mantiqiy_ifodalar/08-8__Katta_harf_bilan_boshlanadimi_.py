# Bir so'z kiriting.
# Agar so'z katta harf bilan boshlansa True, aks holda False.
# Masalan: "Aziz" -> True, "aziz" -> False.
soz = input().strip()
print(soz.istitle() or soz[0].isupper() if soz else Folse)