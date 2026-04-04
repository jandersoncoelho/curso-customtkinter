# Como abrir uma nova janela na sua aplicação - Aula04
from pathlib import Path

import customtkinter as ctk

TITULO_JANELA = "Minha Janela customtkinter - Aula 04"
TAMANHO_JANELA = "400x300"
ICONE_JANELA = "joia_pro_icon.ico"
MODO_APARENCIA = "system"
ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")


def aplicar_tema():
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    ctk.set_appearance_mode(MODO_APARENCIA)


def configurar_janela_principal():
    janela = ctk.CTk()
    janela.title(TITULO_JANELA)
    janela.geometry(TAMANHO_JANELA)
    janela.maxsize(width=1024, height=768)
    janela.minsize(width=300, height=200)
    janela.resizable(width=True, height=False)
    janela.iconbitmap(ICONE_JANELA)
    return janela


def abrir_nova_janela(janela_pai):
    top = ctk.CTkToplevel(janela_pai, fg_color="teal")
    top.title("Nova Janela")
    top.geometry(TAMANHO_JANELA)
    top.iconbitmap(ICONE_JANELA)


def adicionar_botao(janela, texto_botao, comando, posicao_x, posicao_y):
    ctk.CTkButton(
        master=janela,
        text=texto_botao,
        command=comando,
    ).place(x=posicao_x, y=posicao_y)


def main():
    aplicar_tema()
    janela = configurar_janela_principal()
    adicionar_botao(
        janela=janela,
        texto_botao="Nova Janela",
        comando=lambda: abrir_nova_janela(janela),
        posicao_x=100,
        posicao_y=100,
    )
    janela.mainloop()


if __name__ == "__main__":
    main()
