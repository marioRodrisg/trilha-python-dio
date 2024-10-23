# Criamos uma classe caso seja preciso criar funcionalidades para o código,organizar e agrupar.
class Bicicleta: 
    '''essa classe serve de modelo para criação de seus objetos e atributos'''
    # O __init__ deve ser usado sempre no começo da criação da nossa CLASSE
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor # O self é obrigatorio na linguagem python para acessar os atributos.
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    # Esses def são os chamados métodos, são funções que pertecem a uma classe
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Aqui são as instâncias ou objetos que usamos para acessar os metodos da classe
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
