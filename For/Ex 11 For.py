# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# A média de idade do grupo, OK
# Qual a idade do homem mais velho OK
# quantas mulheres tem menos de 20 anos
age_sum = 0
max_man_age = 1
men = 0
woman = 0
for i in range(0, 4):
    name = input("What's your name?")
    sex = str(input("Are you men or woman?"))
    age = int(input("What's your age? "))
    print("=====================================")

    age_sum = age_sum + age
    if sex == "men":
        if age >= max_man_age:
            max_man_age = age
    if sex == "woman":
        if age <= 20:
            woman += 1

age_mean = age_sum / 4
print("The age mean of this group is: {}".format(age_mean))
print("The oldest men in this group has: {} years old".format(max_man_age))
print("The number of woman under 20's is: {}".format(woman))
