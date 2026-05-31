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


class Aula01Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        try:
            # aplicar tema se disponível
            if 'aplicar_tema' in globals():
                aplicar_tema()
        except Exception:
            pass
        # reutiliza os widgets definidos no módulo quando possível
        if 'label' in globals() or True:
            ctk.CTkLabel(self, text="Ola, Mundo!", font=("Arial", 20)).pack(pady=20)
            ctk.CTkButton(self, text="Clique aqui").pack()

if __name__ == "__main__":
    main()
