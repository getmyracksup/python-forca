import requests
from bs4 import BeautifulSoup
from os import system, name
from unidecode import unidecode

tentativas = 5

def clear() -> None:
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

def getPalavra() -> str:
    reqPalavra = requests.get('https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1&fs2=0&Submit=Nova+palavra')
    soup = BeautifulSoup(reqPalavra.text, 'html.parser')

    if not reqPalavra.status_code == 200:
        print('Falha em capturar nova palavra...')
        exit(-1)

    divs = soup.find_all('div')
    divPalavra = divs[1]
    palavraAleatoria = divPalavra.text.strip()
    palavraAleatoria = palavraAleatoria.split(" ")[0]
    return [palavraAleatoria.lower(), unidecode(palavraAleatoria).lower()]

def respostaEmBranco(tamanhoPalavra: int) -> str:
    respostaVazia = ''
    for i in range(tamanhoPalavra):
        respostaVazia += '_'
    return respostaVazia

def filterResposta(palavra: str, resposta: str) -> str:
    posicoes = []
    for i, j in enumerate(resposta):
        if j == "_":
            posicoes.append(i)
    for posicao in posicoes:
        palavra = palavra[:posicao] + '_' + palavra[posicao+1:]
    return palavra

def printMenu(resposta: str, tentativas: int) -> None:
    clear()
    print('Jogo da Forca - Projeto Hefesto (Kauan, Pedro, Bruno e Alexandre) - 1ECR FIAP\n\tComputational Thinking For Engineering\n\tNúmero de letras palavra: %i' %(tamanhoPalavra))
    print('\tPalavra: %s' %(resposta))
    print('\tTentativas: %i' %(tentativas))


palavra = getPalavra()
palavraCopia = palavra[1]
tamanhoPalavra = len(palavra[0])
resposta = respostaEmBranco(tamanhoPalavra)

while tentativas > 0:
    if resposta == palavraCopia:
        print("Parabens! Voce venceu o jogo :)\nPalavra: %s" %(palavra[0]))
        exit(0)

    printMenu(respostaEmBranco(tamanhoPalavra), tentativas) if resposta == "" else printMenu(filterResposta(palavra[0], resposta), tentativas)
    letraUnfilter = input('\tDigite uma letra: ')
    if letraUnfilter != "": 
        letra = letraUnfilter[0].lower()
    else:
        continue
    
    posicoes = []

    if letra in palavra[1]:
        for i, j in enumerate(palavra[1]):
            if j == letra:
                posicoes.append(i)
        for posicao in posicoes:
            resposta = resposta[:posicao] + letra + resposta[posicao+1:]
            palavra[1] = palavra[1][:posicao] + '_' + palavra[1][posicao+1:]
        continue

    tentativas -= 1

print("Voce perdeu :(\nPalavra: %s" %(palavra[0]))