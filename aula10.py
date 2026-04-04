"""Exemplo de uso do widget label dinâmico aula 10."""

from pathlib import Path

import customtkinter as ctk

ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA = "dark"  # "light", "dark", "system"


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
    janela.title("Label Dinâmico - Aula10")
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


def criar_label_estatico(janela):
    """Cria um rótulo estático para a interface."""
    ctk.CTkLabel(
        janela,
        text="Digite algo na caixa de entrada abaixo e clique no botão.",
        text_color="#f0f0f0",
        font=("Arial", 18, "bold"),
    ).pack(pady=(20, 10), padx=20, anchor="center")


def criar_caixa_de_entrada(janela):
    """
    Cria uma caixa de entrada para o usuário digitar texto.

    Args:
        janela: A janela onde a caixa de entrada será adicionada.
    """
    caixa_de_entrada = ctk.CTkEntry(
        janela,
        placeholder_text="Digite algo aqui...",
        width=450,
        height=40,
        font=("Arial", 14, "bold"),
    )
    caixa_de_entrada.pack(pady=10, padx=20, anchor="center")

    return caixa_de_entrada

def criar_botao(janela, label_dinamico, caixa_de_entrada):
    button_enviar = ctk.CTkButton(
        janela,
        text="Enviar",
        command=lambda: on_clicar_botao_enviar(label_dinamico, caixa_de_entrada),
        width=150,
        height=40,
        font=("Arial", 14, "bold"),
    )
    button_enviar.pack(pady=10, padx=20, anchor="center")


def usar_label_dinamico(janela):
    label_dinamico = ctk.CTkLabel(
        janela,
        text="",
        text_color="#011427",
        fg_color="#f0f0f0",
        width=400,
        height=40,
        corner_radius=10,
        font=("Arial", 16, "bold"),
    )
    label_dinamico.pack(pady=10, padx=20, anchor="center")
    return label_dinamico

def on_clicar_botao_enviar(label_dinamico, caixa_de_entrada):
    texto_entrada = caixa_de_entrada.get()
    label_dinamico.configure(text=f"Você digitou: {texto_entrada}")

def main():
    """Ponto de entrada da aplicação."""
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    criar_label_estatico(janela)
    caixa_de_entrada = criar_caixa_de_entrada(janela)
    label_dinamico = usar_label_dinamico(janela)
    criar_botao(janela, label_dinamico, caixa_de_entrada)
    janela.mainloop()


if __name__ == "__main__":
    main()
