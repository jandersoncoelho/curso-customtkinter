"""Janela base reutilizável para aplicações com CustomTkinter."""

import logging
from pathlib import Path
from typing import Any

import customtkinter as ctk

LOGGER = logging.getLogger(__name__)
ARQUIVO_TEMA = Path(__file__).with_name("tema_oceano.json")
ARQUIVO_ICONE = Path(__file__).with_name("joia_pro_icon.ico")
APARENCIAS_VALIDAS = {"Dark", "Light", "System"}
MODO_APARENCIA_PADRAO = "Dark"
TITULO_PADRAO = "Minha Janela customtkinter - Base Form"
LARGURA_PADRAO = 700
ALTURA_PADRAO = 300
LARGURA_MINIMA = 300
ALTURA_MINIMA = 200
LARGURA_MAXIMA = 1024
ALTURA_MAXIMA = 768


class CtkBaseForm(ctk.CTk):
    """Classe base para padronizar a criação de janelas com CustomTkinter."""

    def __init__(
        self,
        *args: Any,
        aparencia: str = MODO_APARENCIA_PADRAO,
        titulo: str = TITULO_PADRAO,
        largura: int = LARGURA_PADRAO,
        altura: int = ALTURA_PADRAO,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.largura = largura
        self.altura = altura
        self.aplicar_tema(aparencia)
        self.configurar_janela(titulo)
        self.centralizar_janela()
        self.montar_interface()

    def aplicar_tema(self, aparencia: str = MODO_APARENCIA_PADRAO) -> None:
        """Aplica o tema visual e o modo de aparência da interface."""
        if ARQUIVO_TEMA.exists():
            ctk.set_default_color_theme(str(ARQUIVO_TEMA))
        else:
            LOGGER.warning("Arquivo de tema não encontrado: %s", ARQUIVO_TEMA)

        aparencia_validada = (
            aparencia if aparencia in APARENCIAS_VALIDAS else MODO_APARENCIA_PADRAO
        )
        ctk.set_appearance_mode(aparencia_validada)

    def configurar_janela(self, titulo: str) -> None:
        """Define as configurações básicas da janela."""
        self.title(titulo)
        self.geometry(f"{self.largura}x{self.altura}")
        self.maxsize(width=LARGURA_MAXIMA, height=ALTURA_MAXIMA)
        self.minsize(width=LARGURA_MINIMA, height=ALTURA_MINIMA)
        self.resizable(width=True, height=False)
        self.definir_icone()

    def definir_icone(self) -> None:
        """Define o ícone da janela, quando o arquivo estiver disponível."""
        if not ARQUIVO_ICONE.exists():
            return

        try:
            self.iconbitmap(str(ARQUIVO_ICONE))
        except Exception as erro:
            LOGGER.warning(
                "Não foi possível definir o ícone da janela: %s", erro)

    def montar_interface(self) -> None:
        """Método de extensão para subclasses criarem e organizarem os widgets."""

    def centralizar_janela(self) -> None:
        """Centraliza a janela na tela."""
        self.update_idletasks()
        posicao_x, posicao_y = self.calcular_posicao_centralizada()
        self.geometry(f"{self.largura}x{self.altura}+{posicao_x}+{posicao_y}")

    def calcular_posicao_centralizada(self) -> tuple[int, int]:
        """Calcula a posição central da janela com base na tela atual."""
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        posicao_x = (largura_tela - self.largura) // 2
        posicao_y = (altura_tela - self.altura) // 2
        return posicao_x, posicao_y


if __name__ == "__main__":
    app = CtkBaseForm(aparencia="Light",
                      titulo="Exemplo de Janela Base",
                      largura=800,
                      altura=400)
    app.mainloop()
