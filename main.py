"""
    Arquivo principal - Projeto CustomTkinter.

    Este script apresenta uma estrutura base para iniciar o projeto com
    CustomTkinter, aplicando tema personalizado e exibindo uma interface
    simples com rótulos e botão de fechamento. Ele pode ser usado como ponto
    de partida para novas aulas ou para o menu principal da aplicação.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

from pathlib import Path

import customtkinter as ctk

ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA = "system"
ICONE_JANELA = "joia_pro_icon.ico"


def aplicar_tema():
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    ctk.set_appearance_mode(MODO_APARENCIA)


def configurar_janela():
    janela = ctk.CTk()
    janela.title("Projeto CustomTkinter")
    janela.geometry("700x420")
    janela.minsize(width=500, height=320)
    janela.iconbitmap(ICONE_JANELA)
    return janela


def montar_interface(janela):
    ctk.CTkLabel(
        master=janela,
        text="Projeto padronizado com tema personalizado",
        font=("Arial", 20),
    ).pack(pady=(40, 12))

    ctk.CTkLabel(
        master=janela,
        text="Altere este arquivo para iniciar sua aula ou menu principal.",
    ).pack(pady=(0, 24))

    ctk.CTkButton(
        master=janela,
        text="Fechar",
        command=janela.destroy,
    ).pack()


def main():
    aplicar_tema()
    janela = configurar_janela()
    montar_interface(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
