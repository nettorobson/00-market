# HORTIFRUTI JCAVI

''' 
Observações/Limitações:

Esta é uma versão para usuário.
Simula a verificação dos itens no estoque, compra, montagem do carrinho e pagamento.
Código sem usar POO. Somente procedural.
Como os produtos são chaves do dicionário, não é possível comprar duas vezes o mesmo produto. Teria que mudar um pouco a estrutura para ajustar isso.
Não fiz uma opção para editar (excluir itens) do carrinho.
Ao final sobrescreve o csv com a última compra. Como é para fins de exercício, não alterei para cada vez gerar um csv novo ou apendar em cada nova compra.
Não consegui encaixar a estrutura 'try except' de uma forma que funcionasse.
Programa carregado no github em sua versão final.

'''

import csv
from modulos import compraNova
from modulos import csvFunc
from modulos import pgtoFunc

carrinho = []
# Simulei abaixo um dicionário como um banco de dados (estoque dos produtos disponíveis): 
estoque = {'Banana':1.99, 'Maçã':2.99, 'Cebola':0.99, 'Batata':1.59, 'Laranja':1.79, 'Alface':0.89, 'Cenoura':1.19, 
'Alho':0.49, 'Pêssego':3.89, 'Cheiro-verde':0.59, 'Mamão':4.99, 'Bergamota':1.99, 'Melancia':5.99, 'Melão':6.99, 'Caju':9.99, 'Rúcula':0.79, 'Pepino':1.19}

while True: # No LOOP WHILE, o loop fica rodando eternamente até que rode um BREAK. Cuidar para não esquecer disso.
    print('\n---------------HORTIFRUTI JCAVI---------------')
    print('Bem-vindo ao sistema online de compras do HORTIFRUTI JCAVI')
    print('\n1. Ver prateleira\n2. Ver seu carrinho\n3. Comprar itens\n4. Pagamento\n5. Sair')
    menu = input('\nEscolha uma das opções acima: ')

    if menu == '1':
        print('\n------------------PRATELEIRA------------------')
        print('A quantidade de produtos disponíveis é de ',len(estoque),'produtos.')
        while len(estoque) != 0:
            print('Produtos disponíveis e respectivos preços:')
            for k,v in estoque.items():
                print("Produto:",k,", Preço Unitário: R$",v)
            print('------------------------------------------')
            break

    elif menu == '2':
        print('\n-----------------CARRINHO-----------------')
        while len(carrinho) != 0:                      
            print('A quantidade de produtos adicionados no carrinho é de',len(carrinho),'produtos.')
            dict_carrinho = (dict(carrinho))
            print("Detalhamento:")
            for k,v in dict_carrinho.items():
                print("Produto adicionado:",k,", Preço Unitário: R$",v)
            print("-----------------TOTAL------------------")
            print("Valor total de suas compras: R$",round(sum(dict_carrinho.values()),2))
            print('--------------------------------------')
            break
        else:
            print('Seu carrinho está vazio.')
            print('------------------------------------------')

    elif menu == '3':
        print('\n------------------COMPRAR ITENS------------------')
        print('A quantidade de produtos adicionados no carrinho é de',len(carrinho),'produtos.')
        while len(estoque) != 0:
            print('Produtos disponíveis e respectivos preços:')
            for k,v in estoque.items():
                print("Produto:",k,", Preço Unitário: R$",v)
            print('------------------------------------------')
            break
        item = input('Digite o produto que você quer comprar: ')
        if item in estoque:
            compraNova(estoque,item,carrinho)
        else:
            print("Produto inválido. Por favor, digite um produto válido.")
        
        display = input("Deseja continuar comprando? 'Sim' ou 'Não'?: ")
        while display == "Sim":
            item = input('Digite o produto que você quer comprar: ') 
            if item in estoque:
                compraNova(estoque,item,carrinho)
                display = input("Deseja continuar comprando? 'Sim' ou 'Não'?: ") # Toda vez que chamar a variável, ela será reescrita
            else:
                print("Produto inválido. Por favor, digite um produto válido.") 
                display = input("Deseja continuar comprando? 'Sim' ou 'Não'?: ")
        if display == "Não":
            print('\n-----------------CARRINHO-----------------')
            print('A quantidade de produtos adicionados no carrinho é de',len(carrinho),'produtos.')
            dict_carrinho = (dict(carrinho))
            print("Detalhamento:")
            for k,v in dict_carrinho.items():
                print("Produto adicionado:",k,", Preço Unitário: R$",v)
            print("-----------------TOTAL------------------")
            print("Valor total de suas compras: R$",round(sum(dict_carrinho.values()),2))
            print('--------------------------------------')      
        else:
            print("Opção inválida.") # Tem uma dessas com problema. Não consegui fazer um looping e chamar o display novamente (line 74).
            display2 = input("Pressione ENTER para voltar ao menu inicial. ") # Aqui ele perde o loop e volta ao menu inicial. 
            # Usei esse desfecho de 'display2' para não ficar quebrado, pois não consegui fazer ele voltar ao loop while 'display'.
        
    elif menu == '4':
        print('\n-------------------PAGAMENTO-------------------')
        print('A quantidade de produtos adicionados no carrinho é de',len(carrinho),'produtos.')
        dict_carrinho = (dict(carrinho))
        print("Detalhamento:")
        for k,v in dict_carrinho.items():
            print("Produto adicionado:",k,", Preço Unitário: R$",v)
        print("-----------------TOTAL------------------")
        print("Valor total de suas compras: R$",round(sum(dict_carrinho.values()),2))
        print('---------------------------------------')
        print("Escolha a forma de pagamento desejada: \n1.Dinheiro (Receba '5%' de desconto. Pagamento na entrega do pedido) \n2.Débito (Receba '5%' de desconto)\
             \n3.Cartão de Crédito (Pagamento online)")
        pgtoFunc(dict_carrinho)
        csvFunc(csv,carrinho)
        break

    elif menu == '5':
        print("\nAcesse mais ofertas do HORTIFRUTI JCAVI nas nossas redes sociais!")
        print('------------------SESSÃO ENCERRADA------------------')    
        break

    else: 
        print('Digite uma opção válida')