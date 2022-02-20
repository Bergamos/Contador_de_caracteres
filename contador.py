from collections import Counter

class Contador():
    def __init__(self, texto):
        self.texto = texto
        aparicoes = Counter(texto.lower())
        total_caractere = sum(aparicoes.values())

        proporcoes = [(letra, frequencia / total_caractere) for letra, frequencia in aparicoes.items()]
        proporcoes = Counter(dict(proporcoes))
        mais_comuns = proporcoes.most_common(10)
        for caractere, proporcao in mais_comuns:
            print(f'{caractere} => {proporcao * 100:.2f}%')

    
        