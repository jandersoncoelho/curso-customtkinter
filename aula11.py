"""Exemplo de uso do widget ctkEntry com tema customizado."""

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
    janela.title("Entry - Aula11")
    janela.iconbitmap("joia_pro_icon.ico")
    janela.resizable(False, False)
    return janela


def centralizar_janela(janela):
    """Centraliza a janela na tela com tamanho fixo."""
    janela.update_idletasks()

    largura = 700
    altura = 300

    posicao_x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    posicao_y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")


def criar_label(janela: ctk.CTk, texto: str):
    """Cria um rótulo estático para a interface."""
    ctk.CTkLabel(
        janela,
        text=texto,
        text_color="#f0f0f0",
        font=("Arial", 18, "bold"),
    ).pack(pady=(20, 10), padx=20, anchor="center")


def criar_caixa_de_entrada(janela: ctk.CTk) -> ctk.CTkEntry:
    """
    Cria uma caixa de entrada para o usuário digitar texto.

    Args:
        janela: A janela onde a caixa de entrada será adicionada.
    """
    entry_ctk = ctk.CTkEntry(
        janela,
        width=300,
        height=40,
        placeholder_text="Digite algo aqui...",
        font=("Arial", 14),
        state="normal",
        corner_radius=10,
    )
    entry_ctk.pack(pady=10, padx=20, anchor="center")
    return entry_ctk


def usar_label_dinamico(janela: ctk.CTk) -> ctk.CTkLabel:
    """Cria um rótulo dinâmico para a interface."""
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
    """Função de exemplo para o botão enviar."""
    texto_entrada = caixa_de_entrada.get()
    label_dinamico.configure(text=f"Você digitou: {texto_entrada}")
    texto_entrada = caixa_de_entrada.delete(0, ctk.END)


def criar_botao(janela: ctk.CTk, label_dinamico: ctk.CTkLabel, caixa_de_entrada: ctk.CTkEntry):
    button_enviar = ctk.CTkButton(
        janela,
        text="Enviar",
        command=lambda: on_clicar_botao_enviar(
            label_dinamico, caixa_de_entrada),
        width=150,
        height=40,
        font=("Arial", 14, "bold"),
    )
    button_enviar.pack(pady=10, padx=20, anchor="center")


def criar_widgets(janela):
    """Cria o rótulo e o Entry com tema customizado."""
    criar_label(janela, "Digite algo na caixa de entrada abaixo e clique no botão.")
    caixa_de_entrada = criar_caixa_de_entrada(janela)
    label_dinamico = usar_label_dinamico(janela)
    criar_botao(janela,
                label_dinamico,
                caixa_de_entrada)


def main():
    """Ponto de entrada da aplicação."""
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    criar_widgets(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
