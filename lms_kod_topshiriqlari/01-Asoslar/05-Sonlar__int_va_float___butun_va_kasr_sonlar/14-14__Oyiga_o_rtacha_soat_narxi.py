# Bir qatorda maosh (int) va oyda ishlangan soat (int) kiriting.
# Bir soat uchun o'rtacha haqni hisoblang: soat_narxi = maosh / soat
# "Hourly: <natija>" ko'rinishida chiqaring.`
maosh,soat = map(int,input().split())
soat_narxi = maosh / soat 
print("Hourly:",soat_narxi)