num1 = 16
num2 = 12
summary = num1 + num2
machpela = num1 * num2
hefresh = num1 - num2
modulo = num1 % num2
print(summary)
print(machpela)
print(hefresh)
print(modulo)

if hefresh == 4:
    print('Gal jealouses at Anna Zack')

if machpela != 191:
    print('Gal jealouses at AnnZack')

GALS = [11, 22, 33, 44, 55, 66]

if 22 in GALS:
    print('GAL is 22 years old')

if 99 not in GALS:
    print('GAL is 99 years old')

GALS.append(77)
GALS.insert(0, 0)
GALS.remove(0)
# Gal.remove(6) # ERROR - 6 is not in list
from_end = GALS[-3]
print(from_end)
temp = GALS[3]
# temp_illegal = GALS[10]   # index out of range

for g in GALS:
    GAL = g + 1
    print(GAL)

for i in range(len(GALS)):
    GALS[i] += 10

print(GALS)
