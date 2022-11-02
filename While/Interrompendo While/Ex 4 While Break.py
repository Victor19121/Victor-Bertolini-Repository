# Crie um programa que leia a idade e sexo de varias pessoas
# A cada pessoa cadastrada o prgrama deve perguntar se o usuario quer ou nao continuar
# no final mostre:
# quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos
age_18 = male = female_20 = 0

while True:
    age = int(input("How old? "))
    gender = str(input("What`s the gender?(M/F) ")).upper().strip()[0]

    if age > 18:
        age_18 = age_18 + 1
    if gender == 'M':
        male += 1
    if gender == 'F' and age < 20:
        female_20 += 1

    again = input('Do you want to continue?(Y/N) ').upper().strip()[0]
    if again == 'N':
        break
        print('=='*35)

print(f"""
There are {age_18} people with more than 18 years,
There are {male} man and
There are {female_20} woman with less than 20 years.
""")


