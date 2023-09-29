class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        
    def lista_endereco(self):
        for end in self.enderecos:
            print(end.rua, end.numero)
        
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
        
d1 = Cliente('maike')
d1.inserir_endereco("Rua b", 123)
d1.inserir_endereco("Rua a", 1234)
d1.inserir_endereco("Rua c", 12345)
d1.inserir_endereco("Rua d", 123456)
d1.lista_endereco()

