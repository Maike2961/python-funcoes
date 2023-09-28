import json

CAMINHO_DO_ARQUIVO = 'class.json'

class Pessoa:
    
    
    def __init__(self, nome, idade, ano_nascimento):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = ano_nascimento 
        
        
p1 = Pessoa("Mayki", 23, 2000)
p2 = Pessoa("Lais", 20, 2000)
p3 = Pessoa("Alessandra", 24, 2000)

db = [vars(p1), vars(p2), p3.__dict__]


def dump():
    with open(CAMINHO_DO_ARQUIVO, "w") as arquivo:
        json.dump(db, arquivo, ensure_ascii=False,indent=2 )
    
if __name__ == "__main__":
    dump()
