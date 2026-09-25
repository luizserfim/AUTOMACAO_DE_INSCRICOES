import unicodedata


def normalizar_nome(nome):
    """
    Normaliza um nome para permitir comparações seguras.

    Exemplo:

    "  João   Gonçalves da Silva "
                ↓
    "JOAO GONCALVES DA SILVA"
    """

    # Garante que estamos trabalhando com texto
    nome = str(nome)

    # Remove espaços no começo e no final
    nome = nome.strip()

    # Remove espaços duplicados
    nome = " ".join(nome.split())

    # Converte para maiúsculas
    nome = nome.upper()

    # Separa letras dos acentos
    nome = unicodedata.normalize(
        "NFD",
        nome
    )

    # Remove os acentos
    nome = "".join(
        caractere
        for caractere in nome
        if unicodedata.category(caractere) != "Mn"
    )

    return nome