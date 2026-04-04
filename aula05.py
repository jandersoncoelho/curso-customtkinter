# Como criar frames posicionados em uma janela - Aula05
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
    janela.title("Minha Janela customtkinter - Aula 05")
    janela.iconbitmap("joia_pro_icon.ico")
    return janela


def centralizar_janela(janela):
    janela.update_idletasks()

    janela.maxsize(width=1024, height=768)
    janela.minsize(width=300, height=200)
    janela.resizable(width=True, height=False)
    janela.update_idletasks()

    width = 1024
    height = 500

    x = (janela.winfo_screenwidth() // 2) - (width // 2)
    y = (janela.winfo_screenheight() // 2) - (height // 2)

    janela.geometry(f"{width}x{height}+{x}+{y}")


def main():
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
