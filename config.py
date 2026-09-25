from pathlib import Path



# ==========================================================
# CAMINHOS DO PROJETO
# ==========================================================

# Pasta principal do projeto
BASE_DIR = Path(__file__).resolve().parent

# Pasta onde ficará a planilha de entrada
PASTA_DADOS = BASE_DIR / "dados"

# Pasta onde serão salvos os resultados
PASTA_RESULTADOS = BASE_DIR / "resultados"

# Pasta dos logs
PASTA_LOGS = BASE_DIR / "Logs"

# ==========================================================
# ARQUIVOS
# ==========================================================

# Planilha contendo as duplas
ARQUIVO_ALUNOS = PASTA_DADOS / "alunos.xlsx"

# Relatório gerado após a execução
ARQUIVO_RELATORIO = PASTA_RESULTADOS / "relatorio_cadastros.xlsx"

# Arquivo de log
ARQUIVO_LOG = PASTA_LOGS / "automacao.log"

# ==========================================================
# SITE
# ==========================================================

# Coloque aqui o endereço da plataforma
URL_SITE = "https://cursos.fdr.org.br/inscricao/maratona/cadastro_dupla.php"

# ==========================================================
# ELEMENTOS HTML
# ==========================================================

# Já identificados na plataforma
ID_ALUNO_1 = "aluno1"
ID_ALUNO_2 = "aluno2"

# Ainda vamos identificar
ID_BOTAO_CADASTRAR = None

# ==========================================================
# TEMPOS DE ESPERA
# ==========================================================

# Tempo máximo para encontrar elementos da página
TEMPO_ESPERA = 15

# Tempo máximo para o campo Aluno 2 carregar
TEMPO_CARREGAMENTO_ALUNO2 = 15


# ==========================================================
# SEGURANÇA
# ==========================================================

# Nesta fase o programa NÃO poderá clicar em Cadastrar.
# Só mudaremos para True depois dos testes.
PERMITIR_CADASTRO = False

