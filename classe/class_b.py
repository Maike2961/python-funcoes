import json

from class_a import CAMINHO_DO_ARQUIVO, Pessoa

with open(CAMINHO_DO_ARQUIVO, "r") as arquivo:
    dado = json.load(arquivo)
    print(dado)
    print()
    d1 = Pessoa(**dado[0])
    print(d1.nome, d1.idade, d1.ano_nascimento)
    print()
    d2 = Pessoa(**dado[1])
    print(d2.nome, d2.idade, d2.ano_nascimento)
    print()
    d3 = Pessoa(**dado[2])
    print(d3.nome, d3.idade, d3.ano_nascimento)
    