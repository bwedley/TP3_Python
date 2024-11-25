def questao_um():
    # Dado um dicionário com as idades de várias pessoas, crie um novo dicionário que contenha apenas as pessoas maiores de idade (18 anos ou mais).
    #código reutilizado to TP2-1
    people_dict = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}
    people_dict2 = {'André': 15, 'Carem': 28, 'Lucas': 30, 'Breno': 16, 'Edson': 31}

    def legal_age(dicti):
        print(dict(filter(lambda person: person[1] >= 18, dicti.items())))
    legal_age(people_dict)
    legal_age(people_dict2)

def questao_dois():
    '''Crie uma função que recebe uma string de palavras separadas por espaços e uma lista de palavras indesejadas.
    A função deve retornar uma nova string, excluindo as palavras que estão na lista de indesejadas.'''
    def words_filter(text, filtered_words):
        texto = text.split()
        applying_filter = list(word for word in texto if word not in filtered_words)
        print(' '.join(applying_filter))
    texto = "O jogo fechou sozinho. Talvez eu precise dar um upgrade no pc"
    palavras_filtradas = ["sozinho", "eu", "um"]
    words_filter(texto, palavras_filtradas)
    
def questao_tres():
    '''
    Escreva uma função que recebe uma string e alterna entre maiúsculas e minúsculas para cada letra,
    começando com a primeira letra em maiúscula (Ex: input: "desenvolvendo habilidades" -> output: "DeSeNvOlVeNdO HaBiLiDaDeS").
    '''
    def upper_lower(text):
        characters = ""
        for i, char in enumerate(text):
            if i % 2 == 0:
                characters += char.upper()
            else:
                characters += char.lower()
        print(characters)
    upper_lower("desenvolvendo habilidades")

def questao_quatro():
    '''
    Crie uma função que receba uma lista de listas e retorne uma nova lista apenas com os elementos únicos presentes nessas listas
    (Ex: lista = [[2,4,6], [4, 5, 1, 6], [2, 2, 6]]; output: [1, 2, 4, 5, 6]).
    '''
    def unique_elements(list):
        unique_list = []
        for extra_list in list:
            for item in extra_list:
                if item not in unique_list:
                    unique_list.append(item)
        unique_list.sort()
        print(unique_list)
    lista = [[2, 4, 6], [4, 5, 1, 6], [2, 2, 6]]
    unique_elements(lista)

def questao_cinco():
    '''
    Crie uma função que recebe duas listas de palavras e retorna uma string onde as palavras das duas listas foram intercaladas.
    Se uma lista for maior que a outra, a função deve adicionar os elementos restantes ao final da string resultante.
    '''
    lista_um = ["eu", "de", "café"]
    lista_dois = ["gosto", "tomar", "da", "manhã"]
    def intercalar_lista(lista_um, lista_dois):
        i = 0
        j = 0
        lista_resultante = []
        string_resultante = " "
        while i < len(lista_um) and j < len(lista_dois):
            lista_resultante.append(lista_um[i])
            lista_resultante.append(lista_dois[j])
            i += 1
            j += 1
        while i < len(lista_um):
            lista_resultante.append(lista_um[i])
            i += 1
        while j < len(lista_dois):
            lista_resultante.append(lista_dois[j])
            j += 1
        print(string_resultante.join(lista_resultante))
    intercalar_lista(lista_um, lista_dois)
questao_cinco()


def questao_seis():
    '''
    Crie uma função que recebe uma lista de palavras e um valor inteiro n.
    A função deve retornar uma lista de duas listas: uma contendo as palavras com comprimento menor ou igual a n,
    e outra contendo as palavras com comprimento maior que n.
    '''
    def sep_by_length(list, n):
        equal_or_lesser_than_n = []
        higher_than_n = []

        for word in list:
            if len(word) <= n:
                equal_or_lesser_than_n.append(word)
            else:
                higher_than_n.append(word)
        print(equal_or_lesser_than_n, higher_than_n)
    sep_by_length(['Paladino', 'Mago', 'Caçador', 'Ladino', 'Guerreiro', 'Bruxo'], 6)

def questao_sete():
    lista_palavras = ["corda", "carro", "bateria", "goiaba"]
    '''
    Crie uma função chamada inserir_palavra que receba uma lista de palavras e uma nova palavra.
    A função deve pedir ao usuário a posição desejada para inserir a nova palavra na lista.
    Se a lista tiver menos de três elementos, insira a nova palavra automaticamente no final da lista. No fim, retorne a lista atualizada.
    '''
    def inserir_palavra(lista_palavras, nova_palavra):
        if len(lista_palavras) < 3:
            lista_palavras.append(nova_palavra)
            print(lista_palavras)
        try:
            posicao_palavra = int(input(f"Qual posição você gostaria de adicionar a palavra {nova_palavra}? de 0 a {len(lista_palavras)}: "))
            if posicao_palavra >= 0 and posicao_palavra <= len(lista_palavras):
                lista_palavras.insert(posicao_palavra, nova_palavra)
                print(lista_palavras)
            else:
                print("Posição inválida, tente novamente")
        except ValueError:
            print("Digito inválido, tente novamente")
    inserir_palavra(lista_palavras, "guitarra")

def questao_oito():
    '''
    Crie uma função chamada combinar_listas que receba duas listas de números e use o método extend para combiná-las em uma única lista.
    A função deve retornar essa lista combinada.
    '''
    lista_um = [0, 1, 2, 3]
    lista_dois = [2, 3, 4, 5]
    def combinar_listas(lista_um, lista_dois):
        lista_combinada = lista_um
        lista_combinada.extend(lista_dois)
        print(lista_combinada)
    combinar_listas(lista_um, lista_dois)
    
def questao_nove():
    '''
    Escreva uma função chamada remover_duplicatas que receba uma lista de palavras
    e remova todas as ocorrências de uma palavra duplicada,mantendo apenas a primeira ocorrência.
    '''
    lista = ["carro", "bateria", "goiaba", "carro", "churrasco", "goiaba"]
    def remover_duplicatas(lista_palavras):
        lista_primeira_ocorrencia = []
        for palavra in lista_palavras:
            if palavra not in lista_primeira_ocorrencia:
                lista_primeira_ocorrencia.append(palavra)
        print(lista_primeira_ocorrencia)
    remover_duplicatas(lista)

def questao_dez():
    '''
    Crie uma função chamada gerenciar_compras que receba uma lista de itens de compras e permita ao usuário remover o último item da lista
    (simulando o cancelamento da última compra) usando a função pop. A função deve exibir a lista de compras atualizada após a remoção.
    OBS: Se a lista estiver vazia, a função deve informar que não há mais itens para remover.
    '''
    lista_compras = ["Macarrão", "Batata", "Abacaxi", "Banana", "Azeitona"]
    def gerenciar_compras(lista_compras):
        while (len(lista_compras) > 0):
            resposta_usuario = input(f"Cancelar a compra de {lista_compras[-1]}? (S/N)(0 para sair): ")
            if (resposta_usuario.lower() == "s"):
                lista_compras.pop(-1)
                print(lista_compras) 
            elif (resposta_usuario.lower() == "n"):
                print(lista_compras)
            elif (int(resposta_usuario) == 0):
                print(lista_compras)
                break
            else:
                print("Entrada inválida, tente novamente")
        if (len(lista_compras) == 0):
            print("não há mais itens para remover")
    gerenciar_compras(lista_compras)

def questao_onze():
    '''
    Crie uma função chamada manipular_string que recebe uma string e realiza as seguintes operações:
    Exibe a string original.
    Solicita ao usuário um índice de início e um índice de fim, e exibe a substring correspondente.
    Exemplo de uso: manipular_string("Python é incrível!")
    '''
    texto = "Python é incrível"
    def manipular_string(texto):
        print(f"string original: {texto}")
        solicitacao_usuario_inicial = int(input(f"Indique um índice inicial de 0 a {len(texto)}: "))
        solicitacao_usuario_final = int(input(f"Indique um índice final de {(solicitacao_usuario_inicial) + 1 } a {len(texto)}: "))
        substring = texto[solicitacao_usuario_inicial:solicitacao_usuario_final]
        print(substring)
    manipular_string(texto)

def questao_doze():
    '''
    Crie uma função gerenciar_lista_compras que recebe uma lista de compras e permite as seguintes operações:
    Digitar "fim" para encerrar.
    Digitar "remover" seguido do nome do produto ou seu índice para remover o item da lista.
    Digitar "adicionar" seguido do índice e do nome do produto para adicionar o item na lista na posição indicada.
    A função deve atualizar a lista conforme as operações do usuário e exibi-la ao final.
    '''
