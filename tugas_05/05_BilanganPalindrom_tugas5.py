# Bilangan Palindrom 05_BilanganPalindrom_tugas5.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program memeriksa apakah suatu bilangan bulat yang dimasukkan adalah palindrom atau bukan

# KAMUS
# bil: int
# isPalindrome: bool
# b1,b2,b3,b4,b5,b6,b7,b8,b9,b10: int

# ALGORITMA

bil = int(input("Masukkan suatu bilangan bulat positif diantara 0 sampai 9999999999 (maksimal 10 digit): "))

isPalindrome = False

# Ekstrak tiap digit dari bil
b1 = bil % (10 ** 1) // (10 ** 0)
b2 = bil % (10 ** 2) // (10 ** 1)
b3 = bil % (10 ** 3) // (10 ** 2)
b4 = bil % (10 ** 4) // (10 ** 3)
b5 = bil % (10 ** 5) // (10 ** 4)
b6 = bil % (10 ** 6) // (10 ** 5)
b7 = bil % (10 ** 7) // (10 ** 6)
b8 = bil % (10 ** 8) // (10 ** 7)
b9 = bil % (10 ** 9) // (10 ** 8)
b10 = bil % (10 ** 10) // (10 ** 9)

# Menerima bilangan dengan 1 digit sampai 10 digit
if 0 <= bil < 10 ** 10:
  if bil < 10 ** 1:
    isPalindrome = True
  elif bil < 10 ** 2:
    if b1 == b2:
      isPalindrome = True
    else: # b1 != b2
      isPalindrome = False
  elif bil< 10 ** 3:
    if b1 == b3:
      isPalindrome = True
    else: # b1 != b3
      isPalindrome = False
  elif bil< 10 ** 4:
    if b1 == b4 and b2 == b3:
      isPalindrome = True
    else: # b1 != b4 or b2 != b3
      isPalindrome = False
  elif bil< 10 ** 5:
    if b1 == b5 and b2 == b4:
      isPalindrome = True
    else: # b1 != b5 or b2 != b4
      isPalindrome = False
  elif bil< 10 ** 6:
    if b1 == b6 and b2 == b5 and b3 == b4:
      isPalindrome = True
    else: # b1 != b6 or b2 != b5 or b3 != b4
      isPalindrome = False
  elif bil< 10 ** 7:
    if b1 == b7 and b2 == b6 and b3 == b5:
      isPalindrome = True
    else: # b1 != b7 or b2 != b6 or b3 != b5
      isPalindrome = False
  elif bil< 10 ** 8:
    if b1 == b8 and b2 == b7 and b3 == b6 and b4 == b5:
      isPalindrome = True
    else: # b1 != b8 or b2 != b7 or b3 != b6 or b4 != b5
      isPalindrome = False
  elif bil< 10 ** 9:
    if b1 == b9 and b2 == b8 and b3 == b7 and b4 == b6:
      isPalindrome = True
    else: # b1 != b9 or b2 != b8 or b3 !+ b7 or b4 != b6
      isPalindrome = False
  else: # bil < 10**10
    if b1 == b10 and b2 == b9 and b3 == b8 and b4 == b7 and b5 == b6:
      isPalindrome = True
    else: # b1 != b10 or b2 != b9 or b3 != b8 or b4 != b7 or b5 != b6
      isPalindrome = False
  
  if isPalindrome:
    print(f"Bilangan bulat {bil} merupakan bilangan palindrom")
  else: # isPalindrome == False
    print(f"bilangan bulat {bil} bukan bilangan palindrom")

else: # 0 > bil or bil > 10**10
  print("Bilangan yang dimasukkan di luar jangkauan")

