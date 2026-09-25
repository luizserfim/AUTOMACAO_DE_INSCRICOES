from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from config import URL_SITE


def iniciar_navegador():
    """
    Inicia o Firefox e acessa a página inicial do sistema.
    """

    print("\nIniciando navegador...")

    opcoes = Options()

    driver = webdriver.Firefox(
        options=opcoes
    )

    driver.maximize_window()

    print("Navegador iniciado com sucesso.")

    print("\nAcessando o sistema...")

    driver.get(URL_SITE)

    return driver


def aguardar_preparacao_manual():
    """
    Aguarda o usuário preparar a página antes da automação.
    """

    print("\n" + "=" * 60)
    print("PREPARAÇÃO MANUAL")
    print("=" * 60)

    input(
        "\n1. Faça o login no Firefox."
        "\n2. Acesse a página de cadastro de duplas."
        "\n3. Selecione a escola."
        "\n4. Aguarde a lista de alunos carregar."
        "\n\nQuando estiver tudo pronto, pressione ENTER..."
    )

    print("\nPreparação concluída.")
    print("Iniciando automação das duplas...")