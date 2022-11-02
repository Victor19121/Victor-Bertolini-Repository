# Crie o nome e o preco de varios produtos
#  o programa devera perguntar se quer continuar. No final mostre
# Qual o total gasto na compra
# quantos produtos custam mais de 1000 reais
# Qual o nome do produto mais barato
more_1000 = price = sum = menor = contador = 0


while True:
    name = str(input("What`s the product? ")).strip()
    price = float(input("How much does it cost? "))
    contador += 1
    # Sum of the products
    sum = sum + price
    # If some product costs more than 1000
    if price > 1000:
        more_1000 = more_1000 + 1
    # What's the name of the cheaper product
    if contador == 1:
        menor = price
    else:
        if price < menor:
            menor = price
            new_name = name


    again = input('Do you want to continue?(Y/N) ').upper().strip()[0]
    if again == 'N':
        print('==' * 35)
        break
    print('*0'*35)
print(f"""The total is R${sum}
There are {more_1000} products that cost more than R$1000.00
The cheaper product costs US${menor} and is {new_name}
""")
