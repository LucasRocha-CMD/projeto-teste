def ler_arquivo():
    return """
    Era uma vez em uma pequena aldeia cercada por montanhas, onde todos conheciam todos. As casas eram feitas de madeira, com telhados de palha, e as ruas eram de terra batida. As crianças corriam e brincavam livremente, enquanto os adultos cuidavam de seus afazeres diários.

    Em um canto da aldeia, havia um grande carvalho, cujas folhas verdes forneciam sombra para os moradores durante os dias quentes de verão. Ao pé do carvalho, costumava sentar-se um velho contador de histórias. Sua barba branca e longa quase tocava o chão, e seus olhos brilhavam com a sabedoria acumulada ao longo dos anos.

    Toda tarde, as crianças se reuniam ao redor do velho carvalho para ouvir as histórias fascinantes que ele contava. Histórias de heróis e vilões, de aventuras em terras distantes, e de magias e mistérios. Cada história era um portal para um mundo diferente, e as crianças ouviam, maravilhadas, a cada palavra.

    Um dia, o velho contador de histórias revelou um segredo para as crianças. Ele disse que dentro do carvalho havia um mundo mágico, acessível apenas àqueles que verdadeiramente acreditavam em suas histórias. As crianças, com os olhos arregalados de entusiasmo, juraram que um dia encontrariam esse mundo mágico e viveriam suas próprias aventuras.

    E assim, a pequena aldeia continuou a viver suas rotinas diárias, mas com um brilho especial nos olhos das crianças que acreditavam nas histórias do velho contador de histórias. Pois elas sabiam que, em algum lugar dentro do grande carvalho, um mundo mágico as aguardava.
    """

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def frequencia_palavras(texto):
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        palavra = palavra.lower().strip(".,!?;:()[]{}\"'")
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

def palavras_extremas(texto):
    palavras = texto.split()
    palavras = [palavra.lower().strip(".,!?;:()[]{}\"'") for palavra in palavras]
    mais_curta = min(palavras, key=len)
    mais_longa = max(palavras, key=len)
    return mais_curta, mais_longa

def gerar_relatorio(nome_arquivo, texto):
    total_palavras = contar_palavras(texto)
    frequencia = frequencia_palavras(texto)
    mais_curta, mais_longa = palavras_extremas(texto)
    
    with open(f'relatorio_{nome_arquivo}', 'w') as relatorio:
        relatorio.write(f"Total de palavras: {total_palavras}\n")
        relatorio.write(f"Frequência de palavras:\n")
        for palavra, contagem in frequencia.items():
            relatorio.write(f"{palavra}: {contagem}\n")
        relatorio.write(f"Palavra mais curta: {mais_curta}\n")
        relatorio.write(f"Palavra mais longa: {mais_longa}\n")

if __name__ == "__main__":
    texto = ler_arquivo()
    nome_arquivo = "texto.txt"
    if texto:
        print(f"Total de palavras: {contar_palavras(texto)}")
        print(f"Frequência de palavras: {frequencia_palavras(texto)}")
        mais_curta, mais_longa = palavras_extremas(texto)
        print(f"Palavra mais curta: {mais_curta}")
        print(f"Palavra mais longa: {mais_longa}")
        gerar_relatorio(nome_arquivo, texto)
        print(f"Relatório gerado com sucesso como 'relatorio_{nome_arquivo}'")
