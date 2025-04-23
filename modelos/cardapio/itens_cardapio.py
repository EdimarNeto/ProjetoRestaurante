from abc import ABC, abstractmethod

class Itens_Cardapio(ABC):
    '''
    Classe abstrata base para itens do cardápio.

    Atributos:
        _nome (str): Nome do item.
        _preco (float): Preço do item.

    Métodos:
        aplicar_desconto(): Método abstrato que deve ser implementado pelas subclasses.
    '''
    def __init__(self, nome, preco):
        '''
        Inicializa o item com nome e preço.

        Args:
            nome (str): Nome do item.
            preco (float): Preço do item.
        '''
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        '''Aplica um desconto no item (a ser implementado pelas subclasses).'''
        pass
    