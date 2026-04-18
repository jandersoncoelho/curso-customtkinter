"""
    Aula 01 - Introdução ao CustomTkinter.

    Neste exemplo, apresentamos os primeiros passos com CustomTkinter,
    incluindo a criação de uma janela principal, um rótulo e um botão com
    tema personalizado. A interface demonstra uma base simples e organizada
    para iniciar aplicações gráficas em Python.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

from pathlib import Path

import customtkinter as ctk

ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA = "system"


def aplicar_tema():
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    ctk.set_appearance_mode(MODO_APARENCIA)


def main():
    aplicar_tema()

    janela = ctk.CTk()
    janela.title("Minha Janela customtkinter - Aula 01")
    janela.geometry("400x300")
    janela.iconbitmap("joia_pro_icon.ico")

    label = ctk.CTkLabel(janela, text="Ola, Mundo!", font=(
        "Arial", 20), text_color_disabled="red")
    label.pack(pady=50)

    button = ctk.CTkButton(janela, text="Clique aqui", bg_color="gray")
    button.pack()

    janela.mainloop()


if __name__ == "__main__":
    main()
