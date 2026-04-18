"""
    Aula 02 - Configurando janelas com CustomTkinter.

    Neste exemplo, exploramos a configuração da janela principal da aplicação,
    definindo tamanho inicial, limites mínimos e máximos, redimensionamento e
    ícone personalizado. A interface serve como base para construir layouts
    mais completos de forma controlada.

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


def configurar_janela():
    janela = ctk.CTk()
    janela.title("Minha Janela customtkinter - Aula 02")
    janela.geometry("400x300")
    janela.maxsize(width=1024, height=768)
    janela.minsize(width=300, height=200)
    janela.resizable(width=True, height=False)
    janela.iconbitmap("joia_pro_icon.ico")
    # janela.iconify()
    # janela.deiconify()
    return janela


def main():
    aplicar_tema()
    janela = configurar_janela()
    janela.mainloop()


if __name__ == "__main__":
    main()
