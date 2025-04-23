# 🍽️ Sabor Express - Sistema de Gerenciamento de Restaurantes

Este é um sistema simples em Python orientado a objetos para gerenciar restaurantes, 
avaliações de clientes e itens de cardápio como pratos, bebidas e sobremesas.

## 📁 Estrutura do Projeto

sabor_express/ 
│ 
├── app.py 
├── modelos/
│ ├── init.py
│ ├── avaliacao.py
│ ├── restaurante.py
│ └── cardapio/
│   ├── init.py
│   ├── itens_cardapio.py
│   ├── bebidas.py 
│   ├── pratos.py
│   └── sobremesas.py

🛠️ Criando os arquivos __init__.py
Você pode criar todos com esses comandos (estando na raiz do projeto):

touch modelos/__init__.py
touch modelos/cardapio/__init__.py

Esses arquivos podem ficar vazios, a menos que você queira exportar explicitamente 
funções ou classes (mais avançado).

## 🚀 Funcionalidades

- Cadastro de restaurantes com nome e categoria
- Avaliação dos restaurantes por clientes (notas de 1 a 5)
- Ativação e desativação de restaurantes
- Cadastro e exibição de itens no cardápio (pratos, bebidas e sobremesas)
- Aplicação de descontos personalizados nos itens
- Exibição da lista de restaurantes com avaliação média e status

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (POO)
- Herança e polimorfismo
- Uso de docstrings e boas práticas
- Abstração com classes abstratas
- Organização modular com pacotes

## 🛠️ Requisitos

- Python 3.10 ou superior
- Ambiente virtual recomendado (venv)

### Criar e ativar ambiente virtual

bash python3 -m venv venvsource venv/bin/activate

▶️ Como executar

1. Clone este repositório
2. Ative o ambiente virtual
3. Execute o arquivo app.py:

python app.py

📌 Exemplo de uso

restaurante = Restaurante("Sabor da Massa", "Pizzaria")
pizza = Prato("Pizza Calabresa", 30.00, "Deliciosa pizza com calabresa artesanal")
restaurante.adicionar_no_cardapio(pizza)
restaurante.receber_avaliacao("Carlos", 5)
restaurante.exibir_cardapio

Autor: Edimar Duarte Neto
Data: 23/04/2025
Versão: 1.0
