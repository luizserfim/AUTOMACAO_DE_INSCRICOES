from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def selecionar_alunos(driver, aluno1, aluno2):
    """
    Localiza a aba correta do cadastro de duplas
    e seleciona os dois alunos.
    """

    print("\nSelecionando alunos...")

    # ------------------------------------------------------
    # DIAGNÓSTICO DAS ABAS/JANELAS
    # ------------------------------------------------------

    print("\n--- DIAGNÓSTICO DE JANELAS ---")

    print(
        "Quantidade de abas/janelas:",
        len(driver.window_handles)
    )

    aba_cadastro_encontrada = False

    # Percorre todas as abas abertas no Firefox
    for numero, janela in enumerate(
        driver.window_handles,
        start=1
    ):
        # Muda o controle do Selenium para esta aba
        driver.switch_to.window(janela)

        print(f"\nJanela {numero}")
        print("URL:", driver.current_url)
        print("Título:", driver.title)

        # Verifica se estamos na página de cadastro de duplas
        if "cadastro_dupla.php" in driver.current_url:
            aba_cadastro_encontrada = True

            print("\nPágina de cadastro de duplas encontrada.")
            break

    # ------------------------------------------------------
    # VERIFICAR SE A PÁGINA FOI ENCONTRADA
    # ------------------------------------------------------

    if not aba_cadastro_encontrada:
        raise RuntimeError(
            "Não foi possível encontrar a página "
            "de cadastro de duplas entre as abas abertas."
        )

    # ------------------------------------------------------
    # LOCALIZAR O PRIMEIRO CAMPO
    # ------------------------------------------------------

    campo_aluno1 = WebDriverWait(
        driver,
        10
    ).until(
        EC.presence_of_element_located(
            (By.ID, "aluno1")
        )
    )

    # ------------------------------------------------------
    # LOCALIZAR O SEGUNDO CAMPO
    # ------------------------------------------------------

    campo_aluno2 = WebDriverWait(
        driver,
        10
    ).until(
        EC.presence_of_element_located(
            (By.ID, "aluno2")
        )
    )

    # ------------------------------------------------------
    # TRANSFORMAR OS CAMPOS EM SELECT
    # ------------------------------------------------------

    seletor_aluno1 = Select(campo_aluno1)
    seletor_aluno2 = Select(campo_aluno2)

    # ------------------------------------------------------
    # SELECIONAR OS ALUNOS
    # ------------------------------------------------------

    seletor_aluno1.select_by_visible_text(aluno1)
    seletor_aluno2.select_by_visible_text(aluno2)

    print("\nAlunos selecionados com sucesso.")
    print(f"Aluno 1: {aluno1}")
    print(f"Aluno 2: {aluno2}")


def clicar_cadastrar(driver):
    """
    Localiza e clica no botão Cadastrar.
    """

    print("\nLocalizando botão Cadastrar...")

    botao_cadastrar = WebDriverWait(
        driver,
        10
    ).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'button[type="submit"].btn.btn-primary'
            )
        )
    )

    print("Botão Cadastrar localizado.")

    botao_cadastrar.click()

    print("Clique realizado.")


def confirmar_alerta(driver):
    """
    Aguarda o alerta de confirmação do cadastro
    e clica automaticamente em OK.
    """

    print("\nAguardando confirmação do cadastro...")

    alerta = WebDriverWait(
        driver,
        10
    ).until(
        EC.alert_is_present()
    )

    # Captura a mensagem antes de fechar o alerta
    mensagem = alerta.text

    print(f"Mensagem recebida: {mensagem}")

    # Equivale a clicar no botão OK
    alerta.accept()

    print("Confirmação aceita.")

    return mensagem