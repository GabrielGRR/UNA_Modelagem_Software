#Atividade 1:
from math import pi

class circle:
    def __init__(self, radius):
        self.radius = radius
                
    def getRadius(self):
        return self.radius

    def getArea(self):
        self.area= pi*(self.radius**2)
        return round(self.area,2)

# circulo1 = circle(50)
# print(circulo1.getArea(), circulo1.getRadius())

# circulo2 = circle(5)
# print(circulo2.getArea(), circulo2.getRadius())

############################################

#Atividade 2:
class jogo:

    #Valores da instancia desta classe jogo
    def __init__(self, titulo, classificacao_etaria, preco):
        self.titulo = titulo
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco
    
    def aplicarDesconto(self, desconto):
        self.preco = self.preco*(1-desconto/100)
        return self.preco
    
    def aumentarPreco(self, aumento):
        self.preco = self.preco*(1+aumento/100)
        return self.preco
    
    def atualizarClassificacao(self, att_class_etaria):
        self.classificacao_etaria = att_class_etaria
        return self.classificacao_etaria

#Menu 'interface'
class Principal:
    def __init__(self):
        self.jogos = {} #dicionário key-OBJECT pair, não é key-value
        self.menu()
        
    def menu(self):
        opcao_invalida = True

        #Mantem o menu ativo enquanto a pessoa não sair dele via opção 6
        while opcao_invalida:
            menu_list = ["----------","Menu:", "1. Novo jogo","2. Desconto no jogo","3. Aumentar preço do jogo", "4. Classificação etária do jogo", "5. Detalhes dos jogos", "6. Sair", "----------"]
    
            #'interface' do menu
            for i in menu_list:
                print(i)
            
            #Se o usuário digitar qualquer coisa que não for um int, o código não quebrará no input
            try:
                opcao = int(input("Escolha uma opção: "))

                if opcao == 1:
                    self.nome_jogo = input("Digite o nome do jogo: ")
                    classificacao_etaria = int(input("Digite a classificação etária: "))
                    preco = float(input("Digite o preço: R$"))
                    self.jogos[self.nome_jogo] = jogo(self.nome_jogo, classificacao_etaria, preco)

                elif opcao == 2:
                    self.desconto = float(input("Digite o desconto: %"))
                    self.jogos[self.nome_jogo].aplicarDesconto(self.desconto)

                elif opcao == 3:
                    self.aumento = float(input("Digite o aumento: %"))
                    self.jogos[self.nome_jogo].aumentarPreco(self.aumento)

                elif opcao == 4:
                    self.classificacao_etaria = int(input("Digite a classificação etária: "))
                    self.jogos[self.nome_jogo].atualizarClassificacao()

                elif opcao == 5:
                    self.consultaJogo = input("Digite o nome do jogo a ser consultado: ")

                    print('Título:', self.jogos[self.consultaJogo].titulo)
                    print('Classificação etária:', self.jogos[self.consultaJogo].classificacao_etaria)
                    preco_jogo = self.jogos[self.consultaJogo].preco
                    print(f'Preço: R${preco_jogo:.2f}' )
                    print('----------')

                elif opcao == 6:
                    print("Saindo...")
                    opcao_invalida = False

                else:
                    print("Opção inválida, digite novamente: ")
            
            except:
                print("----------\nERRO: Favor digitar um número, tente novamente: ")                

principal = Principal()