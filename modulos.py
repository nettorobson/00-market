# def compraNova (Mais simples):
def compraNova(estoque,item,carrinho):
    for kv in estoque.items():
        if item in kv:
            carrinho.append(kv)
            print("Produto adicionado ao carrinho com sucesso")
            print(carrinho)
        else:
            pass

# def pgtoFunc(): Construir essa func semelhante à compraNova()
def pgtoFunc(dict_carrinho):
    pgto_func = input("\nDigite a opção escolhida ('1', '2' ou '3'): ")
    if pgto_func == "1":
        print("-----------------TOTAL------------------")
        print("Valor total de suas compras: R$",round(sum(dict_carrinho.values()),2))
        print("\nDesconto Aplicado!")
        print("\nValor final para pagamento: R$",round((95*sum(dict_carrinho.values())/100),2))
        print("Pagamento concluído com sucesso na modalidade DINHEIRO")
        print("----------------------------------------")
    elif pgto_func == "2":
        print("-----------------TOTAL------------------")
        print("Valor total de suas compras: R$",round(sum(dict_carrinho.values()),2))
        print("\nDesconto Aplicado!")
        print("\nValor final para pagamento: R$",round((95*sum(dict_carrinho.values())/100),2))
        print("Pagamento concluído com sucesso na modalidade DÉBITO")
        print("----------------------------------------")
    elif pgto_func == "3":
        print("-----------------TOTAL------------------")
        print("Valor total de suas compras: R$",round(sum(dict_carrinho.values()),2))
        print("\nValor final para pagamento: R$",round(sum(dict_carrinho.values()),2))
        print("Pagamento concluído com sucesso na modalidade CRÉDITO")
        print("----------------------------------------")
    else:
        print ("Opção inválida. digite uma das opções ('1', '2' ou '3')")
        pgtoFunc(dict_carrinho) # Como boa prática, podemos chamar a função dentro dela mesmo para "forçar" um loop?

# def csvFunc(): Função para criar o csv do carrinho (produtos comprados)
def csvFunc(csv,carrinho):
    with open('compra.csv', 'w') as f:
        fieldnames = ["Produto", "Preço"]
        writer = csv.writer(f, fieldnames)
        writer.writerow(fieldnames)
        for k,v in dict(carrinho).items():
            writer.writerow([k,v])
    print("Pedido encaminhado com sucesso!") 
    print("Acesse mais ofertas do HORTIFRUTI JCAVI nas nossas redes sociais!")
    print('------------------SESSÃO ENCERRADA------------------')