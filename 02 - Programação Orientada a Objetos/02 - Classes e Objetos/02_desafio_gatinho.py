# Irei criar aqui um código próprio para fixar o conteúdo.

class Gato:
    '''classe para trabalhar com gatos'''
    tipo_animal = 'Felino'
    def __init__(self, nome):
        '''Inicializando nossa classe'''  
        self.nome = nome  
        print("\nO nome do seu gatinho é", self.nome)

    def peso_gato(self, peso):
        self.peso = peso
        if self.peso > 5.0:
            print('\nGatinho gordinho')
        elif self.peso <= 3.5:
            print('\nGatinho magrinho')
        else:
            print('\nO peso do gatinho está na média')

    def _dieta_gatinho(self):
        self.msg = 'Tudo ok!'
        if self.peso < 3.5:
            self.msg = 'Aumente a ração do felino!'
        if self.peso >= 5.0:
            self.peso = 'Diminua a ração do felino!'  
        return self.msg

    def dados_gato(self):
        print('\nO gato', self.nome, 'esta com', self.peso, 'kg')
        print(self._dieta_gatinho())  

gato = input("Digite o nome do seu gato: ")
g1 = Gato(gato)

peso_gato = float(input('\nQual o peso do gato? '))
g1.peso_gato(peso_gato)

g1.dados_gato()