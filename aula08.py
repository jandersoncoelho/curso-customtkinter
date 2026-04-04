"""
app = ctk.CTk()
app.geometry("400x300")

def abrir_dialogo():
# Criação da caixa de diálogo
dialog = ctk.CTkInputDialog(title="Caixa de diálogo", text="Digite seu número de celular:")

# Captura e exibição do input
resultado = dialog.get_input()
if resultado:
print(f"Número de celular buscado: {resultado}")
Botão para disparar a função

btn = ctk.CTkButton(app, text="Abrir caixa de diálogo", command=abrir_dialogo)
btn.pack(pady=20)

app.mainloop()
    """

# Aprenda a criar uma caixa de texto de forma correta (Textbox) - Aula07
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
    janela.title(
        "Aprenda a criar caixa de dialogo de forma correta (dialog) - Aula08")
    janela.iconbitmap("joia_pro_icon.ico")
    janela.resizable(False, False)
    btn_abrir_dialogo = ctk.CTkButton(
        janela, text="Abrir caixa de diálogo", command=lambda: abrir_dialogo(janela, btn_abrir_dialogo))
    btn_abrir_dialogo.pack(pady=(200, 0), padx=20, anchor="center")
    return janela


def centralizar_janela(janela):
    janela.update_idletasks()

    width = 1024
    height = 500

    x = (janela.winfo_screenwidth() // 2) - (width // 2)
    y = (janela.winfo_screenheight() // 2) - (height // 2)

    janela.geometry(f"{width}x{height}+{x}+{y}")


def abrir_dialogo(janela, btn=None):
    # Criação da caixa de diálogo
    dialog = ctk.CTkInputDialog(title="Caixa de diálogo",
                                text="Digite seu número de celular:")

    # Captura e exibição do input
    resultado_input = dialog.get_input()
    if resultado_input:
        ctklabel_resultado = ctk.CTkLabel(
            janela, text=f"Número de celular buscado: {resultado_input}")
        ctklabel_resultado.pack(pady=5, padx=20, after=btn, anchor="center")
        print(f"Número de celular buscado: {resultado_input}")


def main():
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
