from modelos.cardapio.itens_cardapio import Itens_Cardapio

class Sobremesa(Itens_Cardapio):
    '''Classe que representa uma sobremesa no cardápio.

    Atributos:
        tipo (str): Tipo da sobremesa (ex: Bolo, Torta).
        tamanho (str): Tamanho da sobremesa.
        descricao (str): Descrição da sobremesa.'''
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        '''Inicializa a sobremesa com nome, preço, tipo, tamanho e descrição.

        Args:
            nome (str): Nome da sobremesa.
            preco (float): Preço da sobremesa.
            tipo (str): Tipo da sobremesa.
            tamanho (str): Tamanho da sobremesa.
            descricao (str): Descrição da sobremesa.'''
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        '''Retorna o nome da sobremesa.

        Returns:
            str: Nome da sobremesa.'''
        return self._nome
    
    def aplicar_desconto(self):
        '''Aplica um desconto de 15% no preço da sobremesa.'''
        self._preco -= (self._preco * 0.15)
