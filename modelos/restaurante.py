from modelos.avaliacao import Avaliacao
from modelos.cardapio.itens_cardapio import Itens_Cardapio

class Restaurante:
    '''
    Classe que representa um restaurante com nome, categoria, status(ativado ou desativado) e uma lista de avaliações.
    Atributos da classe:
        restaurantes (list): Lista com todos os restaurantes instanciados.
    Atributos da instância:
        _nome(str): Nome do restaurante.
        _categoria(str): Categoria do restaurante. (ex: Japonesa, Caseira, etc.)
        _ativo(bool): Indica se o restaurante está ativo ou não.
        _avaliacoes(list): Lista de objetos Avaliacao associados ao restaurante.
    '''
    restaurantes = []

    def __init__(self, nome, categoria):
        '''
        Inicializa um novo restaurante com nome, categoria e status desativado. Também adiciona o restaurante á lista de todos os restaurantes.

        Argumentos:
            nome(str): Nome do restaurante.
            categoria(str): Categoria restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''
        Retorna a representação textual de um restaurante.
        Return:
            str: Nome e categoria do restaurante formatados.
        '''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''
        Imprime uma tabela formatada com todos os restaurantes registrados, mostrando nome, categoria, avaliação, média e status(ativo/desativado).
        '''
        print(f'{'𝙍𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩𝙚𝙨'.ljust(16)} | {'𝘾𝙖𝙩𝙚𝙜𝙤𝙧𝙞𝙖𝙨'.ljust(12)} | {'𝘼𝙫𝙖𝙡𝙞𝙖ç𝙖̃𝙤'} / {'𝙎𝙩𝙖𝙩𝙪𝙨'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(16)} | {restaurante._categoria.ljust(12)} | {str(restaurante.avaliacao_media)} {restaurante.ativo}')

    @property
    def ativo(self):
        '''
        Retorna uma string indicando se o restaurante está ativado ou desativado.
        Returns:
            str: Ativado ou Desativado
        '''
        return '✅ Ativado' if self._ativo else '❎ Desativado'
    
    def alterar_status(self):
        '''
        Alterna o status de ativo para desativado, ou virse-versa.
        '''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
        Adiciona uma nova avaliação ao restaurante se a nota estiver entre 1 e 5.
        Args:
            cliente(str): Nota do cliente que está avaliando.
            nota(int): Nota dada ao restaurante, entre 1 e 5.
        '''
        if 1 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
        else:
            print('⚠️ Nota inválida! Apenas entre 1 e 5')

    @property
    def avaliacao_media(self):
        '''
        Calcula e retorna a média das avaliações do restaurante, com formatação amigável.
        Returns:
            str: Média formatada com emoji e quantidade de avaliações.
        '''
        if not self._avaliacoes:
            return 'Sem avaliações ainda 😕'
        soma = sum(av._nota for av in self._avaliacoes)
        media = round(soma / len(self._avaliacoes), 1)
        return f"Média: {media} ⭐ ({len(self._avaliacoes)} avaliações)"

    def adicionar_no_cardapio(self, item):
        if isinstance(item, Itens_Cardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'\n📋 Cardápio do Restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, 1):
            if hasattr(item, 'descricao'):
                msg_prato = f'{i}. Prato: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(msg_prato)
            elif hasattr(item, 'tamanho'):
                msg_bebida =f'{i}. Bebida: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(msg_bebida)

'''
Docstring
Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.
'''