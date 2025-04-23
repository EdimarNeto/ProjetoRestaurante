from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.pratos import Prato
from modelos.cardapio.sobremesas import Sobremesa

# Restaurante Praça
'''Instanciando e adicionado itens no Restaurante Praca'''
restaurante_praca = Restaurante('Perolas Burguer', 'Gourmet')
bebida_suco = Bebida('Suco de Manga', 5.00, 'Grande')
prato_pao = Prato('Pão de Queijo', 3.00, 'Pãozinho')
sobremesa1 = Sobremesa('Pudim', 3.50, 'Pudim de Chocolate', 'Médio', 'Sonho Doce')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobremesa1)
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
'''Aplicando notas'''
restaurante_praca.receber_avaliacao('Edinho', 5)
restaurante_praca.receber_avaliacao('Pedro', 5)
restaurante_praca.receber_avaliacao('Vitor', 4)

# Restaurante Praça2
'''Instanciando e adicionado itens no Restaurante Praca2'''
restaurante_praca2 = Restaurante('Stop Lanches', 'Lanchonete')

# Restaurante Pizza
'''Instanciando e adicionado itens no Restaurante Pizza'''
restaurante_pizza = Restaurante('Sabor da Massa', 'Pizzaria')
restaurante_pizza.alterar_status()

def main():
    Restaurante.listar_restaurantes()

    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()