"""Agenda 11 - Desenvolvimento de Sistemas I.

Simula o monitoramento de um reservatório com cinco níveis de água.
Autor: Guilherme Gomes Justi.
"""

from colorama import Fore, Style, just_fix_windows_console


# A posição na lista corresponde ao nível menos 1.
MENSAGENS = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
]

# Leituras fictícias, em ordem crescente, sem entrada de dados do usuário.
NIVEIS_SIMULADOS = [1, 2, 3, 4, 5]


def validar_nivel(nivel: int) -> None:
    """Aceita somente números inteiros de 1 a 5."""
    # bool é uma subclasse de int em Python, mas não representa uma leitura.
    if type(nivel) is not int:
        raise TypeError("O nível deve ser um número inteiro de 1 a 5.")
    if not 1 <= nivel <= len(MENSAGENS):
        raise ValueError("Nível fora do intervalo permitido: use de 1 a 5.")


def definir_cor(nivel: int) -> str:
    """Retorna a cor indicada no enunciado para o nível informado."""
    validar_nivel(nivel)
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]
    return cores[nivel - 1]


def formatar_mensagem(nivel: int) -> str:
    """Monta uma mensagem colorida e restaura o estilo ao final."""
    cor = definir_cor(nivel)
    situacao = MENSAGENS[nivel - 1]
    return f"{cor}Nível {nivel}/5 | Situação: {situacao}{Style.RESET_ALL}"


def exibir_nivel(nivel: int) -> None:
    """Exibe no terminal a situação atual da leitura simulada."""
    print(formatar_mensagem(nivel))


def main() -> None:
    """Inicializa o terminal e executa a simulação dos cinco níveis."""
    just_fix_windows_console()
    print("CONTROLE DE NÍVEIS DE ÁGUA")
    print("Reservatório R-01 | Simulação de monitoramento")
    print("-" * 58)

    for nivel in NIVEIS_SIMULADOS:
        exibir_nivel(nivel)

    print("-" * 58)
    print("Simulação concluída. Terminal com estilo padrão.")


if __name__ == "__main__":
    main()
