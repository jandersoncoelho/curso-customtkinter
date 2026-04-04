# Aprenda a criar Tabs (Abas) no CustomTkinter - Aula06
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
    janela.title("Minha Janela customtkinter - Aula 06")
    janela.iconbitmap("joia_pro_icon.ico")
    return janela


def centralizar_janela(janela):
    janela.update_idletasks()

    width = 1024
    height = 500

    x = (janela.winfo_screenwidth() // 2) - (width // 2)
    y = (janela.winfo_screenheight() // 2) - (height // 2)

    janela.geometry(f"{width}x{height}+{x}+{y}")


def criar_tabs(janela):
    tabview = ctk.CTkTabview(janela, corner_radius=20,
                             border_width=2, border_color="#1e90ff",
                             fg_color="#061623", segmented_button_fg_color="#1e90ff",
                             segmented_button_selected_color="#1e90ff", 
                             segmented_button_unselected_color="#061623", 
                             segmented_button_selected_hover_color="#7e96af",
                             anchor="nw")
    tabview.pack(expand=True, fill="both", padx=20, pady=20)
    adicionar_aba(tabview, "Aba 1")
    adicionar_aba(tabview, "Aba 2")
    adicionar_aba(tabview, "Aba 3")
    adicionar_aba(tabview, "Aba 4")


def adicionar_aba(tabview, nome_aba):
    tabview.add(nome_aba)
    tabview.tab(nome_aba).grid_columnconfigure(0, weight=1)
    tabview.tab(nome_aba).grid_rowconfigure(0, weight=1)
    label = ctk.CTkLabel(tabview.tab(nome_aba),
                         text=f"Este é o conteúdo da {nome_aba}")
    label.grid(padx=20, pady=20, sticky="nsew")


def main():
    aplicar_tema()
    janela = configurar_janela()
    criar_tabs(janela)
    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
