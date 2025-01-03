#Cifra de cesar

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#processo = input('Digite "codificar" para codificar sua mensagem ou "descodificar para descodificar sua mensagem."').lower()
funcao = int(input("Digite 1 para criptografar e 2 para descriptografar:"))
msg = input("Digite sua mensagem:").lower()
chave = int(input("Informe o número de codificação:"))


def cesar(funcao, msg_original, chave):

#Função encripitar
    if funcao == 1:
        msg_cod = "" #Iniciando a variavel que irá receber as letras codificadas e montar o texto
    
        for Letra in msg_original: #Este loop seleciona letra por letra da mesnsagem escrita.

            pos_alfa = alfabeto.index(Letra)    #Aqui Letra é = a letra individual escrita na mensagem Ex "a" = 0 (index)
                                                #assim utilizando o index "Letra" na lista alfabeto descobrimos a posição da letra no alfabeto.
       
            index_codificado = (pos_alfa + chave) % len(alfabeto) #o index códificado é a posição(index) da letra original do alfabeto sendo somado com a "chave de criptografia" que muda o index de acordo com a criptografia desejada
            letra_codificada = alfabeto[index_codificado] #após adiquirir o index codificado, utilizamos a variavel letra_codificada para armazenar a letra já criptografada pelo index somada com a chave.
       
            msg_cod = msg_cod + letra_codificada # msg_cod serve como variavel que irá construir a palavra utilizando as letras códificadas anteriormente.
    
        print(f"Mensagem codificada: {msg_cod}")

#Função descriptografar
    else:
        msg_descod = "" 
    
        for Letra in msg_original:

            pos_alfa = alfabeto.index(Letra)

            index_codificado = (pos_alfa - chave) % len(alfabeto)
            letra_codificada = alfabeto[index_codificado]
        
            msg_descod = msg_descod + letra_codificada 
    
        print(f"Mensagem descodificada: {msg_descod}")

cesar(funcao, msg, chave)


#Função encripitar

def encripitar(msg_original, chave):
    
    msg_cod = "" #Iniciando a variavel que irá receber as letras codificadas e montar o texto
    
    for Letra in msg_original: #Este loop seleciona letra por letra da mesnsagem escrita.

       pos_alfa = alfabeto.index(Letra)    #Aqui Letra é = a letra individual escrita na mensagem Ex "a" = 0 (index)
                                           #assim utilizando o index "Letra" na lista alfabeto descobrimos a posição da letra no alfabeto.
       
       index_codificado = (pos_alfa + chave) % len(alfabeto) #o index códificado é a posição(index) da letra original do alfabeto sendo somado com a "chave de criptografia" que muda o index de acordo com a criptografia desejada
       letra_codificada = alfabeto[index_codificado] #após adiquirir o index codificado, utilizamos a variavel letra_codificada para armazenar a letra já criptografada pelo index somada com a chave.
       
       msg_cod = msg_cod + letra_codificada # msg_cod serve como variavel que irá construir a palavra utilizando as letras códificadas anteriormente.
    
    print(f"Mensagem codificada: {msg_cod}")  

def descodificar(msg_original, chave):
    msg_descod = "" #Iniciando a variavel que irá receber as letras descodificadas e montar o texto
    
    for Letra in msg_original: #Este loop seleciona letra por letra da mesnsagem escrita.

       pos_alfa = alfabeto.index(Letra)    #Aqui Letra é = a letra individual escrita na mensagem Ex "a" = 0 (index)
                                           #assim utilizando o index "Letra" na lista alfabeto descobrimos a posição da letra no alfabeto.
       
       index_codificado = (pos_alfa - chave) % len(alfabeto) #o index códificado é a posição(index) da letra original do alfabeto sendo somado com a "chave de criptografia" que muda o index de acordo com a criptografia desejada
       letra_codificada = alfabeto[index_codificado] #após adiquirir o index codificado, utilizamos a variavel letra_codificada para armazenar a letra já criptografada pelo index somada com a chave.
       
       msg_descod = msg_descod + letra_codificada # msg_cod serve como variavel que irá construir a palavra utilizando as letras códificadas anteriormente.
    
    print(f"Mensagem descodificada: {msg_descod}")









