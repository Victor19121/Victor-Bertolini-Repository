# Crie uma tupla com a lista dos 20 primeiros colcados da tabela do campeonato brasileiro de futebol
# na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados, os 4 últimos colocados, a lista em ordem alfabética, A posição da chapecoense.

tabela_campeonato = ("Corinthians", "Atlético Mineiro", "Flamengo", "Bragantino", "Santos", "Fluminense", "São Paulo", "Coritiba", "América-MG", "Botafogo", "Cuiabá", "Ceará", "Internacional", "Avaí", "Palmeiras", "Juventude", "Goiás", "Atlético", "Goianiense", "Fortaleza", "Athletico-PR")

print(f'Os 5primeiros colocados são {tabela_campeonato[0:6]}')
print(f'Os últimos colocados são: {tabela_campeonato[len(tabela_campeonato) - 4:len(tabela_campeonato)]}')
print(sorted(tabela_campeonato))
print(f'O São Paulo está na {tabela_campeonato.index("São Paulo") + 1}° posição')

