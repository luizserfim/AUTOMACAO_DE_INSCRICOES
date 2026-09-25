import pandas as pd

from config import ARQUIVO_ALUNOS

def limpar_nome(nome):
    """
    Remove espaços desnecessários dos nomes.
    """

    nome = str(nome).strip()

    nome = " ".join(nome.split())

    return nome

def listar_abas():

    """
    Retorna todas as abas existentes na planilha.
    """

    if not ARQUIVO_ALUNOS.exists():
        raise FileNotFoundError(f"Planilha não encontrada: \n{ARQUIVO_ALUNOS}")

    arquivo_exel = pd.ExcelFile(
        ARQUIVO_ALUNOS, 
        engine="openpyxl")
    return arquivo_exel.sheet_names

"""
Observar se as abas estão corretas, caso contrário, o programa não funcionará corretamente.
abas = listar_abas()  
print(abas)
"""
def escolher_aba():
    """
    Mostra as abas existentes e permite ao usuário
    escolher qual delas será processada.
    """
    abas = listar_abas()

    if not abas:
        raise ValueError("Nenhuma aba encontrada na planilha.")


    print("\n" + "=" * 60)
    print("ABAS DISPONÍVEIS")
    print("=" * 60)

    for numero, aba in enumerate(abas, start=1):
        print(f"[{numero}] {aba}")

    while True:
        escolha = input(
            "\nEscolha o número da aba que deseja utilizar: "
        ).strip()

        try:
            numero = int(escolha)

            if 1 <= numero <= len(abas):

                aba_escolhida = abas[numero - 1]

                print(
                    f"\nAba selecionada: {aba_escolhida}"
                )

                return aba_escolhida

            print(
                f"Digite um número entre 1 e {len(abas)}."
            )

        except ValueError:

            print(
                "Digite apenas o número correspondente à aba."
            )
def carregar_alunos(nome_aba):
    """
    Carrega os alunos somente da aba selecionada.
    """

    print(
        f"\nLendo alunos da aba: {nome_aba}..."
    )

    df = pd.read_excel(
        ARQUIVO_ALUNOS,
        sheet_name=nome_aba,
        engine="openpyxl"
    )

    # Limpa possíveis espaços dos cabeçalhos
    df.columns = df.columns.str.strip()

    if "Aluno" not in df.columns:
        raise ValueError(
            f'A aba "{nome_aba}" não possui '
            'uma coluna chamada "Aluno".'
        )

    alunos = df["Aluno"]

        # Remove células vazias
    alunos = alunos.dropna()

    # Limpa os nomes
    alunos = alunos.apply(limpar_nome)

    # Remove possíveis strings vazias
    alunos = alunos[alunos != ""]

    alunos = alunos.tolist()

    print(
        f"Alunos encontrados: {len(alunos)}"
    )

    return alunos

def formar_duplas(alunos):
    """
    Forma as duplas seguindo a ordem da aba.

    Caso a quantidade de alunos seja ímpar,
    o último aluno será identificado como
    aluno sem dupla.
    """

    if not alunos:
        raise ValueError(
            "Nenhum aluno foi encontrado."
        )

    duplas = []

    # ------------------------------------------------------
    # VERIFICAR SE EXISTE ALUNO SEM DUPLA
    # ------------------------------------------------------

    aluno_sem_dupla = None

    if len(alunos) % 2 != 0:
        aluno_sem_dupla = alunos[-1]

    # ------------------------------------------------------
    # DEFINIR QUAIS ALUNOS SERÃO USADOS NAS DUPLAS
    # ------------------------------------------------------

    if aluno_sem_dupla:
        alunos_para_duplas = alunos[:-1]
    else:
        alunos_para_duplas = alunos

    # ------------------------------------------------------
    # FORMAR AS DUPLAS
    # ------------------------------------------------------

    for indice in range(0, len(alunos_para_duplas), 2):
        duplas.append(
            {
                "numero": (indice // 2) + 1,
                "aluno1": alunos_para_duplas[indice],
                "aluno2": alunos_para_duplas[indice + 1]
            }
        )

    # ------------------------------------------------------
    # MOSTRAR RESULTADO
    # ------------------------------------------------------

    print(
        f"Duplas formadas: {len(duplas)}"
    )

    if aluno_sem_dupla:

        print("\n" + "=" * 60)
        print("ATENÇÃO: ALUNO SEM DUPLA")
        print("=" * 60)
        print(aluno_sem_dupla)
        print("=" * 60)

        # ------------------------------------------------------
    # RETORNAR RESULTADOS
    # ------------------------------------------------------

    return duplas, aluno_sem_dupla

def carregar_duplas():
    """
    Executa todo o processo de leitura da planilha.

    1. Permite escolher a aba.
    2. Carrega os alunos.
    3. Forma as duplas.
    4. Retorna todas as informações.
    """

    aba = escolher_aba()

    alunos = carregar_alunos(aba)

    duplas, aluno_sem_dupla = formar_duplas(alunos)

    return aba, duplas, aluno_sem_dupla