from modelos.cardapio.itens_cardapio import Itens_Cardapio

class Prato(Itens_Cardapio):
    '''Classe que representa um prato principal no cardápio.

    Atributos:
        descricao (str): Descrição do prato'''
    def __init__(self, nome, preco, descricao):
        '''Inicializa o prato com nome, preço e descrição.

        Args:
            nome (str): Nome do prato.
            preco (float): Preço do prato.
            descricao (str): Descrição do prato.'''
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        '''Retorna o nome do prato.

        Returns:
            str: Nome do prato.'''
        return self._nome
    
    def aplicar_desconto(self):
        '''Aplica um desconto de 5% no preço do prato.'''
        self._preco -= (self._preco * 0.05)
