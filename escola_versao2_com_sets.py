#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.

"""
__version__ = "0.1.1"

# Dados
sala_1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala_2 = ["João", "Antônio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antônio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antônio"]

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança", aula_danca)]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 50)

    # Retornar os alunos da sala 1 que têm interseção com a atividade

    atividade_sala_1 = set(sala_1) & set(atividade)
    atividade_sala_2 = set(sala_2).intersection(atividade)

    print(f"Sala 1 {atividade_sala_1}")
    print(f"Sala 2 {atividade_sala_2}")
    print("-" * 50)
    print()