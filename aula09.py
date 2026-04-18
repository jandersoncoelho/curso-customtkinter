"""
    Aula 09 - OptionMenu com CustomTkinter.

    Neste exemplo, demonstramos como utilizar o widget CTkOptionMenu para
    permitir a seleção de opções em uma lista. A interface apresenta os meses
    do ano e atualiza dinamicamente um rótulo com a escolha do usuário.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

from pathlib import Path

import customtkinter as ctk

ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA = "dark"  # "light", "dark", "system"
MESES = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]


def definir_aparencia(nova_aparencia):
    """Define o modo de aparência da aplicação."""
    ctk.set_appearance_mode(nova_aparencia)


def aplicar_tema():
    """Aplica o tema visual e o modo de aparência global."""
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    definir_aparencia(MODO_APARENCIA)


def configurar_janela():
    """Cria e configura a janela principal da interface."""
    janela = ctk.CTk()
    janela.title("OptionMenu - Aula09")
    janela.iconbitmap("joia_pro_icon.ico")
    janela.resizable(False, False)
    return janela


def centralizar_janela(janela):
    """Centraliza a janela na tela com tamanho fixo."""
    janela.update_idletasks()

    largura = 700
    altura = 400

    posicao_x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    posicao_y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")


def criar_option_menu(janela):
    """Cria o rótulo e o OptionMenu com os meses do ano."""

    ctk.CTkLabel(
        janela,
        text="Exemplo de uso do widget CTkOptionMenu com tema customizado",
        font=("Arial", 18, "bold"),
    ).pack(pady=(20, 10), padx=20, anchor="center")

    ctk.CTkLabel(
        janela,
        text="Selecione um mês de nascimento:",
        font=("Arial", 16, "bold"),
    ).pack(pady=(50, 10), anchor="center")

    ctk.CTkOptionMenu(
        janela,
        values=MESES,
        command=lambda opcao: on_selecionar_opcao_mes_nascimento(
            var_mes, opcao),
        width=300,
        height=40,
        fg_color="#6554e2",
        button_color="#7e96af",
        button_hover_color="#8a81c8",
        corner_radius=20,
        text_color="#f0f0f0",
        font=("Arial", 14, "bold"),
        dropdown_text_color="#f0f0f0",
        dropdown_font=("Arial", 15, "bold"),
        dropdown_fg_color="#6554e2",
        dropdown_hover_color="#7e96af",
        variable=ctk.StringVar(value="Selecione um mês"),
    ).pack(pady=10, padx=20, anchor="center")

    var_mes = ctk.StringVar(value="")
    ctk.CTkLabel(
        janela,
        textvariable=var_mes,
        font=("Arial", 16, "bold"),
        text_color="#7e96af",
    ).pack(pady=10, padx=20, anchor="center")


def on_selecionar_opcao_mes_nascimento(var_mes, opcao):
    """Recebe a opção escolhida no menu e atualiza o rótulo de resultado."""
    var_mes.set(f"Mês selecionado: {opcao}")
    print(f"Mês selecionado: {opcao}")


def main():
    """Ponto de entrada da aplicação."""
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    criar_option_menu(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
