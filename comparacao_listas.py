
def comparar_listas(lista_inicial, lista_final):

    # Transformar listas em conjuntos para usar as operações de conjuntos.
    conjunto_inicial = set(lista_inicial)
    conjunto_final = set(lista_final)

    # Elementos que não mudaram: são aqueles que estão nas duas listas.
    elementos_nao_mudaram = list(conjunto_inicial.intersection(conjunto_final))

    # Novos elementos: estão na lista final, mas não na inicial.
    novos_elementos = list(conjunto_final.difference(conjunto_inicial))

    # Elementos que foram removidos: estavam na lista inicial, mas não na final.
    elementos_removidos = list(conjunto_inicial.difference(conjunto_final))

    print("\n--- Relatório de Comparação de Listas ---")
    print(f"Permanecem os mesmos: {sorted(elementos_nao_mudaram)}")
    print(f"Foram adicionados: {sorted(novos_elementos)}")
    print(f"Foram removidos: {sorted(elementos_removidos)}")
    print("---------------------------------------")

# Exemplo com lista de produtos
print("Comparando duas listas de produtos:")
versao_inicial_produtos = ["Arroz", "Feijão", "Macarrão", "Sal", "Açúcar"]
versao_final_produtos = ["Arroz", "Café", "Macarrão", "Bolacha", "Açúcar", "Leite"]
comparar_listas(versao_inicial_produtos, versao_final_produtos)

# Exemplo com lista de números
print("\nComparando duas listas de números:")
versao_inicial_numeros = [1, 2, 3, 4, 5, 6]
versao_final_numeros = [3, 4, 7, 8, 9]
comparar_listas(versao_inicial_numeros, versao_final_numeros)

# Lista vazia
print("\nComparando uma lista com apenas um item com uma lista vazia:")
comparar_listas(["Maçã"], [])

# Duas listas vazias
print("\nComparando duas listas vazias:")
comparar_listas([], [])

# Listas iguais
print("\nComparando duas listas idênticas:")
comparar_listas(["A", "B", "C"], ["A", "B", "C"])
