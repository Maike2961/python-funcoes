class Carrinho:
    def __init__(self):
        self._produtos = []
        
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
            
    def listar_produto(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
    
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1 = Produto('Caneta', 1.20)
p2 = Produto('Borracha', 0.50)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produto()
print(carrinho.total())
         