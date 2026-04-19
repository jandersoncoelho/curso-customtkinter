import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula15Form(CtkBaseForm):
    """Janela da aula 15 com foco em frames e organização de layout."""

    def __init__(self) -> None:
        super().__init__(
            aparencia="Dark",
            titulo="Frames e Layout - Aula 15",
            largura=800,
            altura=500,
        )
        self.resizable(width=False, height=False)

    def montar_interface(self) -> None:
        """Sobrescreve a base para concentrar toda a estrutura de widgets."""
        # Aqui você pode adicionar frames, botões, labels, etc.
        pass


if __name__ == "__main__":
    aula15 = Aula15Form()
    aula15.mainloop()
