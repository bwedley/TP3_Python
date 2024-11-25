#Para os exercícios abaixo (de 1 a 4), você deve providenciar uma solução utilizando apenas uma linha de código:

#Crie um programa que receba uma lista de números digitados pelo usuário e retorne os quadrados desses números.

def square_number(lista):
    print(list(((x) ** 2 for x in lista)))

square_number([2, 3, 4, 5, 6])

#Crie um programa que recebe uma lista de números e, para cada um desses números, retorna 0 se ele for menor do que 10 ou retorna o próprio número, caso contrário.
def verify_value(lista):
    print(list(0 if x < 10 else x for x in lista))

verify_value([2, 9, 11, 9, 20])

#Crie um programa que receba uma história contada pelo usuário contendo múltiplas frases. O programa deve retornar uma lista com o número de palavras de cada frase dessa história
# (Ex: “Hoje o dia estava ensolarado. Amanhã deve fazer sol também. Ontem e anteontem estava chuvoso ou nublado.” deve retornar [5, 5, 7]).
def user_tale():
    print([len(tale.split()) for tale in input("Conte uma história separando as frases por ponto: ").split('.') if tale.strip()])

user_tale()

#Crie uma lista de diferentes frases (3 ou mais frases) e conte o número de vogais em cada frase.

def counting_vowels(lista):
    print([sum(1 for letra in frase.lower() if letra in "aeiouáéíóúãõâêîôûàèìòù") for frase in lista])
    
counting_vowels([
    "Hoje o dia estava ensolarado.", 
    "Amanhã deve fazer sol também.", 
    "Ontem e anteontem estava chuvoso ou nublado.",
    "Semana passada o horizonte ficou nublado."
])