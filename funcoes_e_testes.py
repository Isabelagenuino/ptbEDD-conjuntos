
def estados_representados(dicionario_cidades):
    # transformando os valores do dicionário em um conjunto
    return set(dicionario_cidades.values())

def estados_em_comum(dict1, dict2):
  
    # Pega os estados de cada dicionário como conjuntos.
    estados1 = set(dict1.values())
    estados2 = set(dict2.values())

    # Intersecção é usado para encontrar o que é comum.
    # Depois transforma de volta em lista e ordena.
    estados_comuns = list(estados1.intersection(estados2))
    estados_comuns.sort()
    return estados_comuns

# Dicionários de cidades
cidades_a = {'Osasco': 'SP', 'Caldas': 'MG', 'Uberaba': 'MG', 'Vitória': 'ES', 'Cláudio': 'MG'}
cidades_b = {'Rio de Janeiro': 'RJ', 'São Paulo': 'SP', 'Belo Horizonte': 'MG', 'Curitiba': 'PR'}
cidades_c = {'Florianópolis': 'SC', 'Porto Alegre': 'RS'}


# Teste da função 'estados_representados'
print(f"Estados que cidades_a representa: {estados_representados(cidades_a)}")
# Deve mostrar: {'ES', 'MG', 'SP'}

print(f"Estados que cidades_b representa: {estados_representados(cidades_b)}")
# Deve mostrar: {'PR', 'RJ', 'MG', 'SP'}

print(f"Estados que cidades_c representa: {estados_representados(cidades_c)}")
# Deve mostrar: {'RS', 'SC'}

print("-" * 35) # Apenas para organizar a saída

# Teste da função 'estados_em_comum'
print(f"Estados que aparecem em cidades_a E cidades_b: {estados_em_comum(cidades_a, cidades_b)}")
# Deve mostrar: ['MG', 'SP']

print(f"Estados que aparecem em cidades_a E cidades_c: {estados_em_comum(cidades_a, cidades_c)}")
# Deve mostrar: [] (nenhum em comum aqui!)

print(f"Estados que aparecem em cidades_b E cidades_c: {estados_em_comum(cidades_b, cidades_c)}")
# Deve mostrar: []
