from colorama import Fore, Style, init

# Inicializa o Colorama para habilitar as cores no terminal.
init(autoreset=False)

# Lista com os cinco níveis do reservatório.
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def exibir_alerta(nivel_informado):
    """Localiza o nível informado e exibe a situação com a cor correspondente."""
    for item in niveis_reservatorio:
        if item["nivel"] == nivel_informado:
            mensagem = (
                f"Nível {item['nivel']} - {item['situacao']}"
            )
            print(item["cor"] + mensagem + Style.RESET_ALL)
            return

    print(Fore.RED + "Erro: nível informado inválido." + Style.RESET_ALL)


def main():
    print("=== SISTEMA DE CONTROLE DE NÍVEIS DE ÁGUA ===")
    print("Simulação dos níveis do reservatório:\n")

    # Valores definidos no código para simular diferentes situações.
    niveis_simulados = [1, 2, 3, 4, 5]

    for nivel in niveis_simulados:
        exibir_alerta(nivel)


if __name__ == "__main__":
    main()
