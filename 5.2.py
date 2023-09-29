word = input("Введите слово из маленьких латинских букв: ")

vowels = 0
consonants = 0
vowelA = 0
vowelE = 0
vowelI = 0
vowelO = 0
vowelU = 0

for letter in word:
    if letter in "aeiou":
        if letter == "a":
            vowelA +=1
        elif letter == "e":
            vowelE +=1
        elif letter == "i":
            vowelI +=1
        elif letter == "o":
            vowelO +=1
        elif letter == "u":
            vowelU +=1
        vowels += 1
    elif letter in "bcdfghjklmnpqrstvwxyz":
        consonants += 1
    else:
        print(False)

print("Количество гласных букв:", vowels, "( a =", vowelA, ", e =", vowelE, ", i =", vowelI, ", o =", vowelO,", u =", vowelU,")")
print("Количество согласных букв:", consonants)