"""
    Aula 14 - Trabalhando com CtkSlider.

    Este arquivo foi criado para exemplificar o uso do widget CtkSlider, 
    demonstrando como configurar um controle deslizante para ajustar valores de forma interativa. 
    A interface inclui um rótulo que exibe o valor atual do slider, permitindo ao usuário 
    visualizar as alterações em tempo real.

    Autor: Janderson de Almeida
    Data: 2026-04-18
"""
from pathlib import Path
import customtkinter as ctk



ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
MODO_APARENCIA = "Dark"  # "light", "dark", "system"

def tocar_musica(caminho_arquivo="musica.mp3"):
    """Toca uma música usando o módulo pydub."""
    try:
        musica = AudioSegment.from_file(caminho_arquivo)
        play(musica)
    except ImportError:
        print("O módulo 'pydub' não está instalado. Instale-o para tocar música.")

def ajustar_volume(valor):
    """Ajusta o volume da música com base no valor do slider."""
    # Esta função pode ser expandida para ajustar o volume da música em tempo real.
    print(f"Volume ajustado para: {valor}%")

def aplicar_tema():
    ctk.set_default_color_theme(str(ARQUIVO_TEMA))
    ctk.set_appearance_mode(MODO_APARENCIA)


def configurar_janela():
    janela = ctk.CTk()
    janela.title("CtkSlider - Aula14")
    janela.iconbitmap("joia_pro_icon.ico")
    janela.resizable(False, False)
    return janela


def centralizar_janela(janela):
    janela.update_idletasks()

    largura = 400
    altura = 200

    posicao_x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    posicao_y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")


def criar_widgets(janela):
    label_valor = ctk.CTkLabel(
        janela, text="Valor do Slider: 0", font=("Arial", 16))
    label_valor.pack(pady=20)

    def atualizar_label(valor):
        label_valor.configure(text=f"Alterar Volume: {int(float(valor))}%")
        ajustar_volume(int(float(valor)))

    slider = ctk.CTkSlider(janela, from_=0, to=100, command=atualizar_label)
    slider.pack(pady=10)

    ctk.CTkButton(janela, text="Play",
                  command=tocar_musica).pack(pady=10)


def main():
    aplicar_tema()
    janela = configurar_janela()
    centralizar_janela(janela)
    criar_widgets(janela)
    tocar_musica("musica.mp3")
    janela.mainloop()


if __name__ == "__main__":
    main()
