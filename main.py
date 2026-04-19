"""
    Arquivo principal - Projeto CustomTkinter.

    Este script apresenta uma estrutura base para iniciar o projeto com
    CustomTkinter, aplicando tema personalizado e exibindo uma interface
    simples com rótulos e botão de fechamento. Ele pode ser usado como ponto
    de partida para novas aulas ou para o menu principal da aplicação.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

import customtkinter as ctk

from ctk_base_form import CtkBaseForm


def montar_interface(janela: CtkBaseForm) -> None:
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


def main() -> None:
    janela_principal = CtkBaseForm(
        aparencia="System",
        titulo="Projeto CustomTkinter",
        largura=700,
        altura=420,
    )
    janela_principal.minsize(width=500, height=320)
    montar_interface(janela_principal)
    janela_principal.mainloop()


if __name__ == "__main__":
    main()
