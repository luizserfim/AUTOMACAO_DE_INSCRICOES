from selenium.common.exceptions import NoSuchElementException

from src.leitor_planilha import carregar_duplas

from src.navegador import (
    iniciar_navegador,
    aguardar_preparacao_manual
)

from src.cadastro import (
    selecionar_alunos,
    clicar_cadastrar,
    confirmar_alerta
)


def main():

    # ------------------------------------------------------
    # 1. ABRIR O FIREFOX UMA ÚNICA VEZ
    # ------------------------------------------------------

    driver = iniciar_navegador()

    # ------------------------------------------------------
    # 2. LOGIN E PREPARAÇÃO INICIAL
    # ------------------------------------------------------

    aguardar_preparacao_manual()

    # ------------------------------------------------------
    # 3. PROCESSAR TURMAS
    # ------------------------------------------------------

    while True:

        # --------------------------------------------------
        # ESCOLHER A TURMA
        # --------------------------------------------------

        nome_aba, duplas, aluno_sem_dupla = carregar_duplas()

        print("\n" + "=" * 60)
        print(f"TURMA: {nome_aba}")
        print("=" * 60)

        print(f"\nQuantidade de duplas: {len(duplas)}")

        if aluno_sem_dupla:
            print(
                f"Aluno sem dupla: {aluno_sem_dupla}"
            )

        # --------------------------------------------------
        # CONTADORES
        # --------------------------------------------------

        duplas_processadas = 0
        duplas_puladas = []

        # --------------------------------------------------
        # CADASTRAR TODAS AS DUPLAS DA TURMA
        # --------------------------------------------------

        for dupla in duplas:

            numero = dupla["numero"]
            aluno1 = dupla["aluno1"]
            aluno2 = dupla["aluno2"]

            print("\n" + "-" * 60)
            print(f"DUPLA {numero}")
            print("-" * 60)

            print(f"Aluno 1: {aluno1}")
            print(f"Aluno 2: {aluno2}")

            try:

                # ------------------------------------------
                # SELECIONAR OS ALUNOS
                # ------------------------------------------

                selecionar_alunos(
                    driver,
                    aluno1,
                    aluno2
                )

                # ------------------------------------------
                # CLICAR EM CADASTRAR
                # ------------------------------------------

                clicar_cadastrar(driver)

                # ------------------------------------------
                # CONFIRMAR O ALERTA AUTOMATICAMENTE
                # ------------------------------------------

                mensagem = confirmar_alerta(driver)

                print(
                    f"\nRetorno do sistema: {mensagem}"
                )

                print(
                    f"Dupla {numero} processada com sucesso."
                )

                duplas_processadas += 1

            # --------------------------------------------------
            # ALUNO NÃO ENCONTRADO
            # --------------------------------------------------

            except NoSuchElementException:

                print("\n" + "!" * 60)
                print(f"DUPLA {numero} NÃO PROCESSADA")
                print("!" * 60)

                print(f"\nAluno 1: {aluno1}")
                print(f"Aluno 2: {aluno2}")

                print(
                    "\nUm ou ambos os alunos não estão "
                    "disponíveis na lista do sistema."
                )

                print(
                    "\nPossíveis motivos:"
                    "\n- aluno já cadastrado anteriormente;"
                    "\n- aluno não consta na lista oficial;"
                    "\n- diferença entre o nome da planilha "
                    "e o nome registrado no sistema."
                )

                print(
                    "\nA dupla será pulada."
                    "\nContinuando para a próxima..."
                )

                duplas_puladas.append(
                    {
                        "numero": numero,
                        "aluno1": aluno1,
                        "aluno2": aluno2,
                        "motivo": "Aluno não disponível na lista"
                    }
                )

                continue

            # --------------------------------------------------
            # OUTROS ERROS
            # --------------------------------------------------

            except Exception as erro:

                print("\n" + "=" * 60)
                print("ERRO INESPERADO DURANTE O CADASTRO")
                print("=" * 60)

                print(f"\nDupla: {numero}")
                print(f"Aluno 1: {aluno1}")
                print(f"Aluno 2: {aluno2}")

                print("\nErro:")
                print(erro)

                print(
                    "\nA automação desta turma foi interrompida "
                    "para evitar cadastros incorretos."
                )

                break

        # --------------------------------------------------
        # RESUMO DA TURMA
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print(f"RESUMO DA TURMA: {nome_aba}")
        print("=" * 60)

        print(
            f"\nDuplas processadas com sucesso: "
            f"{duplas_processadas}"
        )

        print(
            f"Duplas puladas: "
            f"{len(duplas_puladas)}"
        )

        # --------------------------------------------------
        # MOSTRAR DUPLAS PULADAS
        # --------------------------------------------------

        if duplas_puladas:

            print("\n" + "-" * 60)
            print("DUPLAS QUE PRECISAM DE CONFERÊNCIA")
            print("-" * 60)

            for dupla_pulada in duplas_puladas:

                print(
                    f"\nDupla {dupla_pulada['numero']}"
                )

                print(
                    f"Aluno 1: {dupla_pulada['aluno1']}"
                )

                print(
                    f"Aluno 2: {dupla_pulada['aluno2']}"
                )

                print(
                    f"Motivo: {dupla_pulada['motivo']}"
                )

        # --------------------------------------------------
        # ALUNO SEM DUPLA
        # --------------------------------------------------

        if aluno_sem_dupla:

            print("\n" + "-" * 60)
            print("ALUNO SEM DUPLA")
            print("-" * 60)

            print(aluno_sem_dupla)

        # --------------------------------------------------
        # TURMA FINALIZADA
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print(f"TURMA {nome_aba} FINALIZADA")
        print("=" * 60)

        # --------------------------------------------------
        # PERGUNTAR SE DESEJA OUTRA TURMA
        # --------------------------------------------------

        while True:

            resposta = input(
                "\nDeseja realizar o processo "
                "com outra turma? [S/N]: "
            ).strip().upper()

            if resposta in ["S", "N"]:
                break

            print(
                "Opção inválida. "
                "Digite S para Sim ou N para Não."
            )

        # --------------------------------------------------
        # ENCERRAR O PROGRAMA
        # --------------------------------------------------

        if resposta == "N":

            print("\nEncerrando automação...")

            driver.quit()

            print("Programa encerrado com sucesso.")

            break

        # --------------------------------------------------
        # PREPARAR PRÓXIMA TURMA
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("PRÓXIMA TURMA")
        print("=" * 60)

        input(
            "\nPrepare a próxima turma no Firefox."
            "\nSelecione a escola/turma correspondente."
            "\nQuando estiver tudo pronto, pressione ENTER..."
        )


if __name__ == "__main__":
    main()