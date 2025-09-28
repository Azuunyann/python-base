#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.

"""
__version__ = "0.1.0"

# Dados
sala_1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala_2 = ["João", "Antônio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antônio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antônio"]

# Listar alunos em cada atividade por sala
atividade_sala_1 = []
atividade_sala_2 = []

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança", aula_danca)]

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 50)

    atividade_sala_1 = []
    atividade_sala_2 = []

    for aluno in atividade:
        if aluno in sala_1:
            atividade_sala_1.append(aluno)
        elif aluno in sala_2:
            atividade_sala_2.append(aluno)

    print(f"Sala 1 {atividade_sala_1}")
    print(f"Sala 2 {atividade_sala_2}")
    print("-" * 50)
    print()