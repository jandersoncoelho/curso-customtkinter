"""
    Aula 07 - Caixa de texto com CustomTkinter.

    Neste exemplo, mostramos como utilizar o widget CTkTextbox para entrada e
    exibição de textos longos. A interface aplica tema, barras de rolagem e
    personalização visual para oferecer uma experiência de escrita mais rica.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

from pathlib import Path
import customtkinter as ctk

ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA = "dark"  # "light", "dark", "system"


def definir_aparencia(nova_aparencia):
    ctk.set_appearance_mode(nova_aparencia)


def aplicar_tema():
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    definir_aparencia(MODO_APARENCIA)


def configurar_janela():
    janela = ctk.CTk()
    janela.title("Minha Janela customtkinter - Aula 07")
    janela.iconbitmap("joia_pro_icon.ico")
    # janela.resizable(False, False)
    return janela


def centralizar_janela(janela):
    janela.update_idletasks()

    width = 1024
    height = 500

    x = (janela.winfo_screenwidth() // 2) - (width // 2)
    y = (janela.winfo_screenheight() // 2) - (height // 2)

    janela.geometry(f"{width}x{height}+{x}+{y}")


def criar_caixa_texto(janela):

    textbox = ctk.CTkTextbox(janela,
                             width=400, height=352,
                             scrollbar_button_color="#6554e2", scrollbar_button_hover_color="#7e96af",
                             border_color='#655e42',
                             border_width=3,
                             corner_radius=15,
                             fg_color="#f0f0f0",
                             text_color="#000000",
                             font=("Arial", 18, "bold", "italic"),
                             border_spacing=20,
                             activate_scrollbars=True,
                             padx=20, pady=20,
                             )

    textbox.pack(expand=True,
                 side="top",
                 anchor="center",
                 )

    textbox.insert("0.0", "Digite seu texto aqui...\n\n" +
                   "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n"*30)


def main():
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    criar_caixa_texto(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
