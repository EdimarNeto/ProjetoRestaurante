from modelos.cardapio.itens_cardapio import Itens_Cardapio

class Bebida(Itens_Cardapio):
    '''
    Classe que representa uma bebida no cardápio.

    Atributos:
        tamanho (str): Tamanho da bebida (ex: Pequeno, Médio, Grande).
    '''
    def __init__(self, nome, preco, tamaho):
        '''
        Inicializa a bebida com nome, preço e tamanho.

        Args:
            nome (str): Nome da bebida.
            preco (float): Preço da bebida.
            tamanho (str): Tamanho da bebida'''
        super().__init__(nome, preco)
        self.tamanho = tamaho

    def __str__(self):
        '''
        Retorna o nome da bebida.

        Returns:
            str: Nome da bebida.'''
        return self._nome
    
    def aplicar_desconto(self):
        '''Aplica um desconto de 8% no preço da bebida.'''
        self._preco -= (self._preco * 0.08)
