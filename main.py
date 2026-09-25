from src.leitor_planilha import carregar_duplas
from src.normalizador import normalizar_nome
# ==========================================================
# TESTE DO NORMALIZADOR
# ==========================================================

nome_excel = "ANA GABRIELLE PEREIRA DA SILVA"
nome_site = "ANA BEATRIZ PEREIRA DA SILVA"

nome_excel_normalizado = normalizar_nome(nome_excel)
nome_site_normalizado = normalizar_nome(nome_site)

print("\nTESTE DO NORMALIZADOR")
print("=" * 60)

print(f"Excel original:      {nome_excel}")
print(f"Site original:       {nome_site}")

print()

print(f"Excel normalizado:   {nome_excel_normalizado}")
print(f"Site normalizado:    {nome_site_normalizado}")

print()

if nome_excel_normalizado == nome_site_normalizado:
    print("✓ SUCESSO: Os nomes correspondem.")
else:
    print("✗ ERRO: Os nomes são diferentes.")

print("=" * 60)

def main():

    print("=" * 60)
    print("AUTOMAÇÃO - MARATONA DE MATEMÁTICA")
    print("=" * 60)

    try:

        # --------------------------------------------------
        # CARREGAR PLANILHA
        # --------------------------------------------------

        aba, duplas, aluno_sem_dupla = carregar_duplas()

        # --------------------------------------------------
        # MOSTRAR RESULTADO
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("RESULTADO")
        print("=" * 60)

        print(f"\nAba utilizada: {aba}")
        print(f"Quantidade de duplas: {len(duplas)}")

        print("\n" + "=" * 60)
        print("DUPLAS")
        print("=" * 60)

        for dupla in duplas:

            print(f"\nDUPLA {dupla['numero']}")

            print(
                f"Aluno 1: {dupla['aluno1']}"
            )

            print(
                f"Aluno 2: {dupla['aluno2']}"
            )

            print("-" * 60)

        # --------------------------------------------------
        # ALUNO SEM DUPLA
        # --------------------------------------------------

        if aluno_sem_dupla:

            print("\n" + "=" * 60)
            print("ALUNO SEM DUPLA")
            print("=" * 60)

            print(aluno_sem_dupla)

        else:

            print("\nTodos os alunos possuem dupla.")

        # --------------------------------------------------
        # FINALIZAÇÃO
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("TESTE FINALIZADO COM SUCESSO")
        print("=" * 60)

    except Exception as erro:

        print("\n" + "=" * 60)
        print("ERRO DURANTE O TESTE")
        print("=" * 60)

        print(erro)


if __name__ == "__main__":
    main()