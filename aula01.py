"""
    Aula 01 - Introdução ao CustomTkinter.

    Neste exemplo, apresentamos os primeiros passos com CustomTkinter,
    incluindo a criação de uma janela principal, um rótulo e um botão com
    tema personalizado. A interface demonstra uma base simples e organizada
    para iniciar aplicações gráficas em Python.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

import customtkinter as ctk

from ctk_base_form import CtkBaseForm


def main() -> None:
    janela_principal = CtkBaseForm(
        aparencia="System",
        titulo="Minha Janela customtkinter - Aula 01",
        largura=400,
        altura=300,
    )

    label = ctk.CTkLabel(
        janela_principal,
        text="Ola, Mundo!",
        font=("Arial", 20),
        text_color_disabled="red",
    )
    label.pack(pady=50)

    button = ctk.CTkButton(
        janela_principal,
        text="Clique aqui",
        bg_color="gray",
    )
    button.pack()

    janela_principal.mainloop()


if __name__ == "__main__":
    main()
