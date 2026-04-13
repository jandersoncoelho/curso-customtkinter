"""Exemplo de uso do widget CtkButtom com tema customizado."""

from pathlib import Path

import customtkinter as ctk
from PIL import Image

ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA_ESCURO = "Dark"  # "light", "dark", "system"
MODO_APARENCIA_CLARO = "Light"
IMAGEM_BOTAO = ctk.CTkImage(light_image=Image.open("images/day-mode.png"), 
                            dark_image=Image.open("images/dark-mode.png"), 
                            size=(30, 30))


def definir_aparencia(nova_aparencia):
    """Define o modo de aparência da aplicação."""
    ctk.set_appearance_mode(nova_aparencia)


def aplicar_tema():
    """Aplica o tema visual e o modo de aparência global."""
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    definir_aparencia(MODO_APARENCIA_ESCURO)


def configurar_janela():
    """Cria e configura a janela principal da interface."""
    janela = ctk.CTk()
    janela.title("Button - Aula12")
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
        font=("Comic Sans MS", 18, "bold"),
    ).pack(pady=(20, 10), padx=20, anchor="center")


def trocar_aparencia_tema():
    """Alterna entre os modos de aparência claro e escuro."""
    aparencia_atual = ctk.get_appearance_mode()
    if aparencia_atual == MODO_APARENCIA_ESCURO:
        definir_aparencia(MODO_APARENCIA_CLARO)
    else:
        definir_aparencia(MODO_APARENCIA_ESCURO)


def criar_botao(janela: ctk.CTk):
    """Cria um botão na janela para alternar entre temas claro e escuro.
    Este botão, quando clicado, dispara a função de alteração de aparência
    da interface, permitindo que o usuário mude dinamicamente entre os temas
    disponíveis.
    Args:
        janela(ctk.CTk): A instância da janela principal onde o botão será inserido.
    Returns:
        None
    Raises:
        None
    """
    ctk.CTkButton(janela,
                  text="Clique para trocar o tema",
                  width=300,
                  height=70,
                  fg_color="#d0d0d0",
                  text_color="#011427",
                  hover_color="#0e592d",
                  font=("Comic Sans MS", 16, "bold"),
                  border_color="#0e592d",
                  border_width=2,
                  corner_radius=20,
                  border_spacing=5,
                  state="normal",
                  image=IMAGEM_BOTAO,
                  command=trocar_aparencia_tema).pack(pady=30)


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
        font=("Times New Roman", 16, "bold"),
    )
    label_dinamico.pack(pady=10, padx=20, anchor="center")
    return label_dinamico


def on_clicar_botao_enviar(label_dinamico, caixa_de_entrada):
    """Função de exemplo para o botão enviar."""
    texto_entrada = caixa_de_entrada.get()
    label_dinamico.configure(text=f"Você digitou: {texto_entrada}")
    texto_entrada = caixa_de_entrada.delete(0, ctk.END)


def criar_widgets(janela):
    """Cria o rótulo e o Entry com tema customizado."""
    criar_label(
        janela, "Clique no botão.")
    criar_botao(janela)


def main():
    """Ponto de entrada da aplicação."""
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    criar_widgets(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
