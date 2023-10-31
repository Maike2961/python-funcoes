class Controle:
    def __init__(self, cor,largura,altura,profundidade):
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.profundidade = profundidade
                
    def passar_canal(self, botao):
        if(botao == "+"):
            print("Aumentar o canal")
        elif(botao == "-"):
            print("diminuir o canal")
        else:
            print("Botão errado")
            
""" bot = Controle("Preto", "4cm", "10cm", "2cm")
print(bot.cor)
bot.passar_canal("+") """
            
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ["basic", "premium"]
        if plano in self.lista_plano:
            self.plano = plano
        else:
            print("Plano invalido")
    
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
            
    def ver_filme(self, filme, plano_filme):
        if plano_filme == self.plano:
            print(f"Ver filme {filme}")
        elif plano_filme == "premium" and self.plano == "basic":
            print("faça a atualização para premium pra assistir")
        else:
            print("Plano invalido")
    
usuario = Cliente("Iykam", "fulano@gmail.com", "basic")
usuario.mudar_plano("premium")
usuario.ver_filme("Rambo", "basic")
print(usuario.plano)
        
        


        