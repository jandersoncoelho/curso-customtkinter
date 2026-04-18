"""
    Aula 03 - Personalização de tema no CustomTkinter.

    Neste exemplo, mostramos como aplicar um tema visual personalizado e
    definir o modo de aparência da aplicação. O código destaca uma estrutura
    simples para padronizar a interface e melhorar a experiência visual do
    usuário.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

from pathlib import Path

import customtkinter as ctk

ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA = "system"


def definir_aparencia(nova_aparencia):
    ctk.set_appearance_mode(nova_aparencia)


def aplicar_tema():
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    definir_aparencia(MODO_APARENCIA)


def configurar_janela():
    janela = ctk.CTk()
    janela.title("Minha Janela customtkinter - Aula 03")
    janela.geometry("400x300")
    janela.maxsize(width=1024, height=768)
    janela.minsize(width=300, height=200)
    janela.resizable(width=True, height=False)
    janela.iconbitmap("joia_pro_icon.ico")
    return janela


def main():
    aplicar_tema()
    janela = configurar_janela()
    janela.mainloop()


if __name__ == "__main__":
    main()
