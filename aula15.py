import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula15Form(CtkBaseForm):
    """Janela da aula 15 com foco em frames e organização de layout."""

    def __init__(self) -> None:
        super().__init__(
            aparencia="Dark",
            titulo="SegmentedButton - Aula 15",
            largura=800,
            altura=500,
        )
        self.resizable(width=False, height=False)

    def opcao_selecionada(self, valor: str) -> None:
        """Exibe o valor selecionado no console."""
        print(f"Opção selecionada: {valor}")

    def montar_interface(self) -> None:
        """Sobrescreve a base para concentrar toda a estrutura de widgets."""
        ctk.CTkLabel(
            self,
            text="Aula 15 - Estudando segmented button",
            text_color="#F0F0F0",
            font=("Arial", 20, "bold"),
        ).pack(pady=(20, 10))
        
        segment_button = ctk.CTkSegmentedButton(
            self,
            values=["Opção 1", "Opção 2", "Opção 3"],
            command=self.opcao_selecionada,
            bg_color="#000033",
            fg_color="#555555",
            selected_color="#007ACC",
            text_color="#F0F0F0",
        
        )
        segment_button.pack(pady=20)    


if __name__ == "__main__":
    aula15 = Aula15Form()
    aula15.mainloop()
