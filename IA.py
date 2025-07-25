import sorteio as srt

with open('palavras_comuns.txt', 'r', encoding='utf-8') as arquivo:
    palavras = [srt.remover_acentos(linha.strip()) for linha in arquivo if linha.strip()]

ultimo_resultado = ""
ultima_palavra_usada = ""

letras_eliminadas = []
letras_presentes = []
letras_com_posicao_correta = []

palavras_possiveis = palavras.copy()

def captar_resultado(palavra, resultado):
    global ultimo_resultado, ultima_palavra_usada
    ultimo_resultado = resultado
    ultima_palavra_usada = palavra

def fazer_tentativa(tentativa):
    global letras_eliminadas, letras_presentes, letras_com_posicao_correta

    if tentativa == 0:
        return "aureo"
    else:
        for i, simbolo in enumerate(ultimo_resultado):
            letra = ultima_palavra_usada[i]
            if simbolo == "#":
                if letra not in letras_eliminadas:
                    letras_eliminadas.append(letra)
            elif simbolo == "?":
                if letra not in letras_presentes:
                    letras_presentes.append(letra)
            elif simbolo == "!":
                if (letra, i) not in letras_com_posicao_correta:
                    letras_com_posicao_correta.append((letra, i))

        if tentativa < 2:
            eliminar_palavras(redundancia=False)
        else:
            eliminar_palavras(redundancia=True)

        if palavras_possiveis:
            print(palavras_possiveis)
            return palavras_possiveis[0]

def palavra_valida(palavra):
    for letra, i in letras_com_posicao_correta:
        if palavra[i] != letra:
            return False
    for letra in letras_presentes:
        if letra not in palavra:
            return False
    for letra in letras_eliminadas:
        if letra in palavra:
            return False
    return True

def eliminar_palavras(redundancia=False):
    global palavras_possiveis

    base = palavras_possiveis if redundancia else palavras

    nova_lista = []
    for palavra in base:
        if palavra_valida(palavra):
            nova_lista.append(palavra)

    if redundancia:
        palavras_possiveis = list(set(palavras_possiveis) & set(nova_lista))
    else:
        palavras_possiveis = nova_lista
