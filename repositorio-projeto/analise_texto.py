def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        return None

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
    nome_arquivo = input("Digite o nome do arquivo de texto: ")
    texto = ler_arquivo(nome_arquivo)
    if texto:
        gerar_relatorio(nome_arquivo, texto)
        print(f"Relatório gerado com sucesso como 'relatorio_{nome_arquivo}'")
